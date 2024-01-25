from os import path, listdir, makedirs, system
from utils import clean_version

src_path = path.abspath("src_notebooks")
notebook_path = path.abspath("notebooks")
for script_name in listdir(src_path):
    if not script_name.startswith("."):  # Ignore hidden files
        print(f"Making {script_name}...")
        # Convert to notebook
        basename = path.splitext(script_name)[0]
        makedirs(path.join(notebook_path, basename), exist_ok=True)
        teacher_ipynb_path = path.join(notebook_path, basename, f"{basename}_teacher.ipynb")
        student_ipynb_path = path.join(notebook_path, basename, f"{basename}_student.ipynb")
	
        print(teacher_ipynb_path)
        print(student_ipynb_path)

        system(f'jupytext "{path.join(src_path, script_name)}" --to notebook -o "{teacher_ipynb_path}"')
        system(f'jupytext "{path.join(src_path, script_name)}" --to notebook -o "{student_ipynb_path}"')

        clean_version(teacher_ipynb_path, version="teacher")
        clean_version(student_ipynb_path, version="student")
