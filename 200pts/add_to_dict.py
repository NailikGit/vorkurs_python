def typ():
    a: str = input("    var: ")
    b: str = input("    type: ")
    
    match b:
        case "bool":
            a: bool = bool(a)
        case "int":
            a: int = int(a)
        case "str":
            pass
        case "float":
            a: float = float(a)
        case "chr":
            try:
                a: int = int(a)
                a: chr = chr(a)
            except:
                pass
        case "list":
            a: list[str] = list(a)

    return a


if __name__ == "__main__":
    print("key: ")
    a = typ()
    print("val")
    b = typ()

    dickt: dict = {a:b}

    print(dickt)