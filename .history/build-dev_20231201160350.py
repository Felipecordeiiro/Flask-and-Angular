import os 
import subprocess
import time

current_directories = os.getcwd()
directories = os.listdir(current_directories)
non_angular_dirs = ['static', 'templates', 'flask']

for root, dirs, files in os.walk(directories):
     if "." not in dirs and dirs not in non_angular_dirs:
        angular_project_path = os.path.join(current_directories, dirs)
        dist_path = os.path.join(angular_project_path, 'dist', dirs)

flask_static_path = os.path.join(current_directories, 'static')
flask_template_path = os.path.join(current_directories, 'templates')

subprocess.call(('cd' + angular_project_path + ' && ng build --watch --base-href /static/ &'), shell=True)
 
dir_exist=True

while dir_exist: 
    try: 
        files = os.listdir(dist_path)
        static_files=''
        html_files=''
        for file in files:
            if file.endswith('.js') or file.endswith('.js.map') or file.endswith('.ico'):
                
    except: