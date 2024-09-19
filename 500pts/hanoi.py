class TuermeVonHanoi():
    count: int
    size: int
    stapel_list: list[list[int]]
    
    def __init__(self, n: int):
        self.count = 0
        self.size = n
        self.stapel_list = [[] for i in range(0, 3)]
        for i in range(self.size, 0, -1):
            self.stapel_list[0].append(i)
    
    def __str__(self) -> str:
        print(self.stapel_list)
        r: str = ""
        for i in range(self.size - 1, -1, -1):
            for j in self.stapel_list:
                se: str = ""
                sb: str = ""
                try:
                    if j[i]:
                        sb = (self.size - j[i]) * " " + (j[i]) * "-"
                        se = (j[i]) * "-" + (self. size - j[i]) * " "
                    else:
                        sb = self.size * " "
                        se = sb
                    
                    r += sb + str(j[i]) + se

                except:
                    sb = self.size * " "
                
                    r += sb + str(0) + sb



            r += "\n"
        return r

    def move(self, origin: int, to: int):
        if origin < 0 or origin > 2: raise Exception("tower doesn't exist")
        if to < 0 or to > 2: raise Exception("tower doesn't exist")
        
        if self.stapel_list[origin]:
            a: int = self.stapel_list[origin].pop()
            if self.stapel_list[to]:
                if self.stapel_list[to][len(self.stapel_list[to]) - 1] < a:
                    self.stapel_list[origin].append(a)
                    raise Exception("illegal move")
                else:
                    self.stapel_list[to].append(a)
                    self.count += 1
            else:
                self.stapel_list[to].append(a)
                self.count += 1

        
        

    def status(self) -> bool:
        r1: int = 0
        r2: int = 0
        l: list[int] = [i for i in range(self.size, 0, -1)]
        for i in l:
            if i in self.stapel_list[1]:
                r1 += 1
            if i in self.stapel_list[2]:
                r2 += 1
        b: bool = ((r1 == self.size) or (r2 == self.size))
        if b:
            print("you've won!", end = " ")
            if self.count == (2**self.size - 1):
                print("and optimally at that!")
        return b

    def reset(self):
        self.__init__(self.size)


def game(plates: int):
    t = TuermeVonHanoi(plates)
    print(t)

    while True:
        if t.status(): break
        a = int(input("move plate from tower: ")) - 1
        b = int(input("to tower: ")) - 1
        t.move(a, b)
        print(t)


if __name__ == "__main__":
    plates: int = int(input("number of plates: "))
    game(plates)