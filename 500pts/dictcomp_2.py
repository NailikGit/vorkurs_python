if __name__ == "__main__":
    d: dict[int, int] = {n:{m:n * m for m in range(1, 11)} for n in range(1, 11)}
    print(d)