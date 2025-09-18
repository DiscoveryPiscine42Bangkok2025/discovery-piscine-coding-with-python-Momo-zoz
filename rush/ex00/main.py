from checkmate import checkmate

def main():
    board1 = """\
R...
.K..
..P.
...."""

    board2 = """\
..
.K\
"""

    board3 = """\
..K.
..R.
....
....
"""

    board4 = """\
....
.K..
....
.Q.."""

    board5 = """\
R.P.
.K..
....
...."""

    board6 = """\
B.P.
.K..
....
...."""

    board7 = """\
....
.K.Q
....
...."""



    print("Board 1:")
    checkmate(board1)

    print("Board 2:")
    checkmate(board2)

    print("Board 3:")
    checkmate(board3)

    print("Board 4:")
    checkmate(board4)

    print("Board 5:")
    checkmate(board5)

    print("Board 6:")
    checkmate(board6)

    print("Board 7:")
    checkmate(board7)

    
    
    

if __name__ == "__main__":
    main()