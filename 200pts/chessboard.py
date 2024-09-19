def chessboard(n: int = 8, m: int = 8):
    even: bool = True
    for counter in range(0, n):
        chessrow = ""
        if even:
            for j in range(0, m):
                if j % 2 == 0:
                    chessrow += "#"
                else:
                    chessrow += "O"
        if not even:
            for j in range(0, m):
                if j % 2 == 0:
                    chessrow += "O"
                else:
                    chessrow += "#"
        print(chessrow)
        even = not even

if __name__ == "__main__":
    chessboard(8, 8)
