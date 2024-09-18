if __name__ == "__main__":
    l: list[str] = ["sinep", "mOngo"]
    l = [i.lower() for i in l]
    d: dict[str, str] = {a:{b:a.count(b) for b in a} for a in l}

    s: str = ""
    for k, v in d.items():
        s += k
    d2: dict[str, int] = {a:s.count(a) for a in s}

    #d2 = {inner_k:outer_k.count(inner_k) for (outer_k, outer_v) in d.items() for (inner_k, inner_v) in outer_v.items()}
    print(d)
    #print(d.items())
    print(d2)

    c: int = 0
    for k, v in d2.items():
        c = max(c, v)
    r: str = ""
    for k, v in d2.items():
        if v == c:
            r = k
    print(r)
