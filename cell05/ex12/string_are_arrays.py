import sys

if len(sys.argv) != 2:
    print("none")
else:
    parameter = sys.argv[1]

    count = parameter.count('z')

    if count == 0:
        print("none")
    else:
        print('z' * count)