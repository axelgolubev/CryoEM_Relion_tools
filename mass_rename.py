# Script for a mass rename of the .star files. 
# Change all dots to underscores, except .start extension

import os
file_path = os.getcwd() + '/folder_with_files'
files = os.listdir(file_path)

for file in files:
    new_name_no_ext = file[0:-5].replace('.', '_')
    final = new_name_no_ext + '.star'
    os.rename(file_path + '/' + file, file_path + '/' + final)
