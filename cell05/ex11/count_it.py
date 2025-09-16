import sys

param = len(sys.argv) - 1

if param == 0:
    print("none")
else:
    print(f"parameters: {param}")
    for p in sys.argv[1:]:
        print(f"{p}: {len(p)}")