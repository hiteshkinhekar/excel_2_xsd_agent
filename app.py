from flask import Flask, request, send_file, render_template
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    file = request.files['file']
    if file.filename == '':
        return 'No file selected', 400
    if not file.filename.lower().endswith('.xlsx'):
        return 'Invalid file type. Please upload an .xlsx file.', 400

    # Save to input/
    input_path = os.path.join('input', file.filename)
    file.save(input_path)

    # Output path
    output_filename = file.filename.replace('.xlsx', '.xsd')
    output_path = os.path.join('output', output_filename)

    # Run the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    python_cmd = os.path.join(script_dir, '.venv', 'Scripts', 'python.exe')

    # python_cmd = 'c:/Users/hitesh.kinhekar/OneDrive - Accenture/Documents/Use_Cases/excel_2_xsd_agent/.venv/Scripts/python.exe'
    result = subprocess.run([python_cmd, 'scripts/generate_xsd.py', input_path, output_path], capture_output=True, text=True)

    if result.returncode != 0:
        return f'Error generating XSD: {result.stderr}', 500

    # Return the XSD file for download
    return send_file(output_path, as_attachment=True, download_name=output_filename)

if __name__ == '__main__':
    app.run(debug=True)