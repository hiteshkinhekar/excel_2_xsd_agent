import pandas as pd
import xml.etree.ElementTree as ET
from pathlib import Path

EXCEL_FILE = 'SAMPLE_XSD_CP020.xlsx'
OUTPUT_FILE = 'cp020.xsd'

LEVEL_COLUMNS = [f'Level {i}' for i in range(1, 14)]

SCHEMA_NAMESPACE = 'http://www.eurexchange.com/technology'
INCLUDE_SCHEMA = 'prisma_report_data_types.xsd'


def normalize_occ(v, default='1'):
    if pd.isna(v):
        return default
    s = str(v).strip()
    if s == '':
        return default
    if s.lower() in ('unbounded', 'n'):
        return 'unbounded'
    try:
        x = float(s)
        if x.is_integer():
            return str(int(x))
        return str(x)
    except Exception:
        return s


def find_level_name(row):
    for idx, col in enumerate(LEVEL_COLUMNS, start=1):
        if col in row and pd.notna(row[col]) and str(row[col]).strip() != '':
            return idx, str(row[col]).strip()
    return None, None


def build_hierarchy(df):
    stack = []  # list of (level, node, sequence)
    root = None

    for _, row in df.iterrows():
        level, name = find_level_name(row)
        if name is None:
            continue

        element = ET.Element('xsd:element')
        element.set('name', name)
        element.set('type', f'{name}Type')
        element.set('minOccurs', normalize_occ(row.get('Min', 1), default='1'))
        element.set('maxOccurs', normalize_occ(row.get('Max', 1), default='1'))

        # Attach to parent nest as required.
        while stack and stack[-1][0] >= level:
            stack.pop()

        if stack:
            parent_level, parent_el, parent_seq = stack[-1]
            # parent is no longer leaf; remove generated type
            if 'type' in parent_el.attrib:
                del parent_el.attrib['type']

            if parent_seq is None:
                complex_type = ET.Element('xsd:complexType')
                sequence = ET.Element('xsd:sequence')
                complex_type.append(sequence)
                parent_el.append(complex_type)
                stack[-1] = (parent_level, parent_el, sequence)
                parent_seq = sequence
            parent_seq.append(element)
        else:
            root = element

        # New element may have children; keep track of its sequence placeholder.
        stack.append((level, element, None))

    return root


def generate_xsd(df, output_file):
    root_elem = build_hierarchy(df)
    if root_elem is None:
        raise SystemExit('No root element found in the Excel input')

    ET.register_namespace('xsd', 'http://www.w3.org/2001/XMLSchema')

    schema = ET.Element('{http://www.w3.org/2001/XMLSchema}schema', {
        'xmlns': SCHEMA_NAMESPACE,
        'targetNamespace': SCHEMA_NAMESPACE,
        'elementFormDefault': 'qualified',
    })

    include = ET.Element('{http://www.w3.org/2001/XMLSchema}include', {
        'schemaLocation': INCLUDE_SCHEMA,
    })
    schema.append(include)
    schema.append(root_elem)

    ET.indent(schema, space='\t')
    tree = ET.ElementTree(schema)

    temp_file = output_file + '.tmp'
    tree.write(temp_file, encoding='UTF-8', xml_declaration=False, short_empty_elements=True)

    with open(output_file, 'w', encoding='UTF-8') as f_out, open(temp_file, 'r', encoding='UTF-8') as f_in:
        f_out.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
        f_out.write(f_in.read())

    Path(temp_file).unlink()


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print('Usage: python generate_xsd.py <excel-file> <output-xsd>')
        sys.exit(1)

    input_excel = sys.argv[1]
    output_xsd = sys.argv[2]

    df = pd.read_excel(input_excel, header=1)
    generate_xsd(df, output_xsd)
    print('XSD generated as', output_xsd)

