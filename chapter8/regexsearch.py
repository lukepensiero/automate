import os, re, sys

if len(sys.argv) != 2:
    sys.exit("Incorrect format: py.exe regexsearch.py <regular expression>")
else:
    searchEx = re.compile(sys.argv[1])

for file_name in os.listdir('.'):
    if file_name.endswith('.txt'):
        txt_file = open(file_name)

        lines = txt_file.readlines()

        for line in lines:
            if searchEx.search(line):
                print line

        txt_file.close()
