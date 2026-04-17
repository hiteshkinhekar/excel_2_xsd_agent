---
name: excel_2_xsd
description: Converts Excel files to XSD schema using a Python script, with both command-line and web interface options.
argument-hint: Path to the Excel file to convert to XSD (e.g., "input/sample.xlsx") or "web" to start the web interface.
# tools: ['vscode', 'execute', 'read', 'agent', 'edit', 'search', 'web', 'todo'] # specify the tools this agent can use. If not set, all enabled tools are allowed.
---

This custom agent performs Excel to XSD conversion using the `generate_xsd.py` script located in the `scripts/` directory. It supports both direct command-line conversion and a web-based interface for file uploads.

## Behavior
1. **Command-line Conversion**:
   - Accepts an Excel file path as input (relative to the workspace root).
   - Validates that the input file exists in the workspace.
   - Runs the `generate_xsd.py` script with the provided Excel file as input.
   - Generates the XSD output file in the `output/` directory with a name derived from the input file (e.g., `sample.xsd` for `input/sample.xlsx`).
   - Reports the successful generation and provides the path to the output XSD file.

2. **Web Interface**:
   - When invoked with "web" argument, starts a Flask web server.
   - Provides a web page at `http://127.0.0.1:5000/` for uploading Excel files.
   - Handles file uploads, runs the conversion script, and allows downloading the generated XSD file.

## Capabilities
- Reads Excel files with hierarchical data structured in level columns (Level 1 to Level 13).
- Generates XSD schema with proper element hierarchy, minOccurs/maxOccurs attributes.
- Handles complex type definitions and sequences.
- Includes schema namespace and includes external schema references as defined in the script.
- Provides a user-friendly web interface for file uploads and downloads.
- Validates file types and handles conversion errors gracefully.

## Instructions for Operation
- Ensure the workspace has the required Python dependencies: pandas, openpyxl, flask (use `pip install -r requirements.txt`).
- For command-line conversion: Provide the Excel file path relative to workspace root.
- For web interface: Use "web" as the argument to start the server.
- The input Excel file should have a header row starting from row 1, with columns for levels (Level 1 to Level 13), Min, Max, etc.
- The agent will use the `run_in_terminal` tool to execute the Python script or start the web server.
- If the script fails, the agent should report the error and suggest fixes (e.g., missing dependencies, invalid Excel format).
- For deployment to other machines, follow the instructions in `README.md`.
