# Selective Copy -- copies specific file types from a dir into a new copy path
# selectivecopy.py <path to be copied> <path for new copies> <type of file (include '.')>

import shutil, os, sys

script, base_path, copy_path, file_type = sys.argv

for folder, subfolders, filenames in os.walk(base_path):

    for filename in filenames:

        if filename.endswith(file_type):
            
            print "Copying %s..." % filename
            shutil.copy(os.path.join(folder, filename), copy_path)
