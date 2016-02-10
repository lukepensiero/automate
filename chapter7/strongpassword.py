#   Practice Projects: Strong Password Detection
#   https://automatetheboringstuff.com/chapter7/

import re

def isstrong(pw):
    strong = re.compile(r'''(
        ^
        (?=.*[A-Z])
        (?=.*[0-9])
        (?=.*[a-z])
        .{8,}
        $
        )''', re.VERBOSE)

    return bool(strong.match(pw))

print isstrong(raw_input("Please enter a password: "))
