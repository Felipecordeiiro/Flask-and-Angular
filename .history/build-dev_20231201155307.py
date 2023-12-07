import os 
import subprocess
import time

current_directories = os.getcwd()
directories = os.listdir(current_directories)
non_angular_dirs = ['static', 'templates', 'flask']

for os.walk()in directories