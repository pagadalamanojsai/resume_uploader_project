import os

structure = {
    "app": {
        "__init__.py": "",
        "main.py": "",
        "upload.py": "",
        "extract.py": "",
        "database.py": "",
        "sheets_reader.py": "",
        "batch_process.py": ""
    },
    "data": {},
    "tests": {
        "test_extract.py": "",
        "test_upload.py": ""
    },
    ".env": "SUPABASE_URL=\nSUPABASE_KEY=\n",
    "requirements.txt": "",
    ".gitignore": "env/\n__pycache__/\n.env\n*.pyc\n*.pdf\ncredentials.json\n"
}

def create_structure(base_path, tree):
    for name, contents in tree.items():
        path = os.path.join(base_path, name)
        if isinstance(contents, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, contents)
        else:
            with open(path, 'w') as f:
                f.write(contents)

create_structure(".", structure)
print("✅ Project structure created.")
