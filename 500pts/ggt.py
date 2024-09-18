def euclid(a: int, b: int) -> int:
    l: list[int] = [a, b]
    while not (b == 0):
        l.append(a % b)
        a = b
        b = l[len(l) - 1]
    print(l)
    return a

if __name__ == "__main__":
    print(euclid(12, 4))
    print(euclid(4, 12))
    print(euclid(-12, 4))