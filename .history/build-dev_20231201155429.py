import os 
import subprocess
import time

current_directories = os.getcwd()
directories = os.listdir(current_directories)
non_angular_dirs = ['static', 'templates', 'flask']

for root, dirs, files in os.walk(directories):
     if "." not in dirs and dirs not in non_angular_dirs:
          