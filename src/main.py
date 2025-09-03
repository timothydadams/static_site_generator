import os, shutil
from copy_static_content import copy_files_recursively
from generate_content import generate_page, generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print("deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    print("copying static files to public directory...")
    copy_files_recursively(dir_path_static, dir_path_public)

    print("generating html pages...")
    
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public
    )


main()