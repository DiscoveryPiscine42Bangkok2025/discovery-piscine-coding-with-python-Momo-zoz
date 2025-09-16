import sys

params = sys.argv[1:]

if not params:
    print("none")
else:
    for word in params:
        match word:
            case p if p.endswith("ism"):
                pass
            case _:
                print(f"{word}ism")