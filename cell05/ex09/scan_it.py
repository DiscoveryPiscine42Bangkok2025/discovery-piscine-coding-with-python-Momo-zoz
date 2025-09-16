import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    string = sys.argv[2]
    occurrences = re.findall(rf"{re.escape(keyword)}", string)
    if occurrences:
        print(len(occurrences))
    else:
        print("none")
