if __name__ == '__main__':
    a = [1,2,3,4,5,6]
    if len(a)>20:
        print("Riesig")
    elif len(a)<21 and len(a)>10:
        print("Groß")
    else:
        print("klein")
