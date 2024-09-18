if __name__ == "__main__":
    l: list[list] = [[] for column in range(0, 5)]
    i: int = 0
    for list in l:
        for j in range(0, 5):
            list.append(int(j == 2 or i == 2))
        i += 1

    print(l)