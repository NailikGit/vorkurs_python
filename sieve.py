def prim(max: int) -> list[int]:
    """Returns all prime numbers up to 'max'"""
    max -= 1
    l: list[bool] = []
    r: list[int] = []
    for i in range(0, max):
        l.append(False)
    
    for i in range(0, max):
        if not l[i]:
            r.append(i + 2)
            for j in range(((i + 2) * (i + 2)) - 2, max, i + 2):
                l[j] = True
        
    return r

if __name__ == '__main__':
    max: str = input("Max: ")
    if(max):
        max: int = int(max)
        print(prim(max))
    else:
        print(prim(100))

#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#[2, 3, 5, 7, 13, 17, 19, 23, 25, 29, 35, 37, 43, 47, 49, 53, 59, 65, 67, 73, 77, 79, 85, 89, 95]