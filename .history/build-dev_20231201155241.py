import os 
import subprocess
import time

current_director = os.getcwd()
directories = os.listdir(current_directorie)
non_angular_dirs = ['static', 'templates', 'flask']