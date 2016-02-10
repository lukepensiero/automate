# Filling in the gaps -- Scans a specified dir for files with specified prefix, removes any 'gaps' in numbering by renaming files
# fillgaps.py <dir to scan> <prefix of files to de-gap>
import os, sys, shutil

script, path, prefix = sys.argv

os.chdir(path)

counter = 1

for filename in os.listdir('.'):

    if filename.startswith(prefix):
        numbering = filename[len(prefix):filename.rfind('.')]

        if int(numbering) != counter:
            scounter = str(counter)
            
            shutil.move(filename, os.path.join(os.getcwd(), filename[0:len(prefix)] + scounter.rjust(3, '0') + filename[filename.rfind('.'):len(filename)]))

        counter += 1
