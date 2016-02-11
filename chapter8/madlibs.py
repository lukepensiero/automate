#! /usr/bin/python

# Automate the Boring Stuff -- Chapter 8
# Practice Projects: Mad Libs
# Create a Mad Libs style game where the user change can the text for select words located in a specified madlibs.txt file

import re

# Helper function to prompt user input to replace matched text
def replacer(matchObj):
        return raw_input("Enter an %s: " % matchObj.group(0).lower())

def playMadLibs():
    word_ex = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')

    readFile = open('madlibs.txt', 'r')
    writeFile = open('yourmadlibs.txt', 'w')

    text = readFile.read()

    # Use compiled regex to find the Mab Libs keywords, then call the helper replacer for each match
    text = word_ex.sub(replacer, text)

    writeFile.write(text)

    print text

    readFile.close()
    writeFile.close()

def main():
    playMadLibs()

if __name__ == '__main__':
    main()
