if __name__ == '__main__':
    n = input("Gib einen Integer ein. ")
    n = int(n)
    s = input("Gib einen Namen ein")
    if n == 2:
        print(f"Juhu")
    elif n < 2 and s == 'Cyber':
        print(f"Yeah")
    elif n > 2 or s == "Felix":
        print(f"Jippi")
    elif s == "Marc":
        print("Heureka")
    else:
        print("jay")
