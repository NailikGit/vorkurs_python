if __name__ == '__main__':
    a = input('gib eine zahl ein: ')
    try:
        a = int(a)
        if a >= 5 and a <= 10:
            print('yipii')
        else:
            print('nooo')
    except:
        print('das keine zahl')

    
