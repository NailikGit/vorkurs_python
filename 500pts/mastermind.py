def check(pL: list[int], pG: list[int]) -> (int, int):
    """Checks the correctness of the guess"""
    l: list[int] = pL.copy()
    g: list[int] = pG.copy()
    r: list[int] = []
    rc: int = 0
    n: int = 4
    for i in l:
        if i in g:
            r.append(i)
            rc += 1

    for i in r:
        g.remove(i)
        l.remove(i)

    if rc == 4:
        global run
        run: bool = False

    rp: int = 0
    for i in g:
        if i in l:
            rp += 1

    return rc, rp

#deprecated
#def checkpresent(l, g):
#    r = 0
#    for i in range(0, 4):
#        for j in range(0, 4):
#            if i == j:
#                continue
#            if l[i] == g[j]:
#                r += 1
#    return r


if __name__ == "__main__":
    mastermind: list[int] = [4, 9, 8, 6]
    global run
    run: bool = True

    while(run):
        a: str = input("Gib eine vierstellige Zahl ein: ")
        a: int = [int(b) for b in a]

        b, c = check(mastermind, a)

        print(f"{b} Ziffern sind korrekt.")
        print(f"{c} Ziffern sind vorhanden,"
              + " aber an der falschen Position.")
    print("Du hast die richtige Kombination")
