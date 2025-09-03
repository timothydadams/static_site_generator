import os
import shutil

def copy_files_recursively(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for file in os.listdir(source_dir):
        from_path = os.path.join(source_dir, file)
        dest_path = os.path.join(dest_dir, file)
        print(f" * {from_path} --> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursively(from_path, dest_path)