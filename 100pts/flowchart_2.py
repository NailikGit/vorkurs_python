if __name__ == '__main__':
    n = input("hallo")
    n = int(n)
    if n < 0:
        print("fehler")
    else:
        fakultaet = 1
        while n > 1:
            fakultaet = fakultaet * n
            n = n - 1
        print(fakultaet)