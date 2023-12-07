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

flask