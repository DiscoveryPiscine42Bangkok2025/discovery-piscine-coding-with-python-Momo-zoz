def checkmate(board: str):
    rows = [r.strip() for r in board.splitlines() if r.strip() != ""]
    n = len(rows)
    if n == 0 or any(len(r) != n for r in rows):
        print("Fail")
        return

    king = None
    for i in range(n):
        for j in range(n):
            if rows[i][j] == 'K':
                king = (i, j)
                break
        if king:
            break
    if not king:
        print("Fail")
        return
    
    krow, kcolumn = king

    def clear_path(r, c, krow, kcolumn):
        drow = 0 if krow == r else (1 if krow > r else -1)
        dcolumn = 0 if kcolumn == c else (1 if kcolumn > c else -1)
        r += drow; c += dcolumn
        while (r, c) != (krow, kcolumn):
            if rows[r][c] != '.':
                return False
            r += drow; c += dcolumn
        return True

    for r in range(n):
        for c in range(n):
            piece = rows[r][c]
            if piece == '.' or piece == 'K':
                continue
            if piece == 'P':
                if r == krow + 1 and abs(c - kcolumn) == 1:
                    print("Success"); return

            elif piece == 'B':
                if abs(krow - r) == abs(kcolumn - c) and clear_path(r, c, krow, kcolumn):
                    print("Success"); return
            elif piece == 'R':
                if (krow == r or kcolumn == c) and clear_path(r, c, krow, kcolumn):
                    print("Success"); return
            elif piece == 'Q':
                if (abs(krow - r) == abs(kcolumn - c) and clear_path(r, c, krow, kcolumn)) or ((krow == r or kcolumn == c) and clear_path(r, c, krow, kcolumn)):
                    print("Success"); return
    print("Fail")