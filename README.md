# Excel to XSD Converter

This project provides a web-based interface for converting Excel files to XSD schemas using a Python script.

## Features

- Upload Excel (.xlsx) files via a web interface
- Automatically generates XSD schema based on the Excel structure
- Downloads the generated XSD file

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone or download this repository to your local machine.

2. Navigate to the project directory:
   ```
   cd path/to/excel_2_xsd_agent
   ```

3. Create a virtual environment (recommended):
   ```
   python -m venv .venv
   ```

4. Activate the virtual environment:
   - On Windows: `.venv\Scripts\activate`
   - On macOS/Linux: `source .venv/bin/activate`

5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/`

3. Upload an Excel file (.xlsx) using the web form.

4. The XSD file will be generated and downloaded automatically.

## Excel File Format

The Excel file should have:
- A header row starting from row 1
- Columns for hierarchical levels (Level 1 to Level 13)
- Columns for Min and Max occurrences
- Other relevant schema information

## Deployment to Other Machines

To deploy this application to another machine:

1. Ensure Python 3.8+ is installed on the target machine.

2. Copy the entire project directory to the target machine.

3. Follow the installation steps above on the target machine.

4. Run the application as described in the Usage section.

## VS Code Agent

This project also includes a custom VS Code agent for Excel to XSD conversion. The agent definition is in `.github/agents/excel_2_xsd.agent.md`. To use the agent in VS Code:

1. Open the project in VS Code.
2. The agent should be available in GitHub Copilot Chat.

## Troubleshooting

- If you encounter import errors, ensure all packages are installed in the virtual environment.
- Make sure the Excel file follows the expected format.
- Check the console output for any error messages during conversion.