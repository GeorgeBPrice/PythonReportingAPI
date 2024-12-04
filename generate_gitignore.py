# Create a .gitignore file with typical Python ignores
gitignore_content = """
# Byte-compiled files
*.pyc
__pycache__/

# Virtual environment
venv/
env/

# Environment variables
.env
*.env

# Jupyter Notebook checkpoints
.ipynb_checkpoints

# macOS metadata files
.DS_Store

# Logs
*.log

# SQLite database
*.sqlite3

# Quarto files
*.qmd-rendered

# Temporary files
.temp_reports/

# Editor directories
.idea/
.vscode/
*.egg-info/
"""

# Write to .gitignore file
with open(".gitignore", "w") as file:
    file.write(gitignore_content)

print(".gitignore file generated successfully.")
