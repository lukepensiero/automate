import re

def regstrip(string, char=' '):

    escapes = re.compile(r'[^A-Za-z0-9\s\t\n\r\f\v]')

    if escapes.match(char):
        regex = '^\\' + char + '?(.*)\\' + char + '$'
    else:
        regex = r'^' + char + '?(.*)' + char + '$'

    strip = re.compile(regex)

    return strip.sub(r'\1', string)

print regstrip(" Bananas ")
print regstrip("Avacadoa", 'a')
print regstrip("todayt", 't')
print regstrip("?toosoon?", "?")
