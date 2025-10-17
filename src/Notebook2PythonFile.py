import json

# Load the notebook content
with open(notebook_path, "r", encoding="utf-8") as notebook_file:
    notebook_json = json.load(notebook_file)

# Extract code cells and convert to a Python script
python_script_content = ""
for cell in notebook_json.get("cells", []):
    if cell.get("cell_type") == "code":
        python_script_content += "\n".join(cell.get("source", [])) + "\n\n"

# Save as a Python file
with open(python_script_path, "w", encoding="utf-8") as script_file:
    script_file.write(python_script_content)

# Provide the converted Python file
python_script_path
