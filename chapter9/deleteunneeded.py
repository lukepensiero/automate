# Deleted unneeded files - deletes files greater than a specified size in the specified dir
# deleteunneeded.py <dir> <file threshold in MB>

import os, sys

script, path, size_threshold = sys.argv

size_threshold = int(sys.argv[2])

for folder, subfolders, filenames in os.walk(path):

    for filename in filenames:

        file_path = os.path.join(folder, filename)

        if os.path.getsize(file_path) > size_threshold * 1000000:
            print "%s is greater than %iMB" % (file_path, size_threshold)
            # os.unlink(file_path)
