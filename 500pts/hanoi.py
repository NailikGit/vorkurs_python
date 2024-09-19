class TowersOfHanoi():
    """class that models the towers of hanoi game including iterative solver"""
    count: int
    size: int
    tower_list: list[list[int]]
    
    def __init__(self, n: int):
        """constructor"""
        self.count = 0
        self.size = n
        self.tower_list = [[] for i in range(0, 3)]
        for i in range(self.size, 0, -1):
            self.tower_list[0].append(i)
    
    def __str__(self) -> str:
        """adds string representation of the towers of hanoi"""
        print(self.tower_list)
        r: str = ""
        for i in range(self.size - 1, -1, -1):
            for j in self.tower_list:
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
        """moves the uppermost plate from tower 'origin' to tower 'to'"""
        if origin < 0 or origin > 2: raise Exception("tower doesn't exist")
        if to < 0 or to > 2: raise Exception("tower doesn't exist")
        
        if self.tower_list[origin]:
            a: int = self.tower_list[origin].pop()
            if self.tower_list[to]:
                if self.tower_list[to][len(self.tower_list[to]) - 1] < a:
                    self.tower_list[origin].append(a)
                    raise Exception("illegal move")
                else:
                    self.tower_list[to].append(a)
                    self.count += 1
            else:
                self.tower_list[to].append(a)
                self.count += 1

    def search(self, n: int) -> int:
        """returns the number of the tower, that contains 'n', defaults to -1, if 'n' doesn't exist"""
        for i in range(0, 3):
            if n in self.tower_list[i]:
                return i
        return -1

    def moveR(self, origin: int):
        """moves element from 'origin' one tower to the right (with wrapping)"""
        match origin:
            case 0:
                self.move(0, 1)
            case 1:
                self.move(1, 2)
            case 2:
                self.move(2, 0)

    def moveL(self, origin: int):
        """moves element from 'origin' one tower to the left (with wrapping)"""
        match origin:
            case 0:
                self.move(0, 2)
            case 1:
                self.move(1, 0)
            case 2:
                self.move(2, 1)

    def solve_iterative(self):
        """solves the towers of hanoi using an iterative algorithm"""
        i = 1
        while not self.status():
            for j in range(0, self.size):
                if (i & 2**j):
                    if j % 2 == 0:
                        self.moveL(self.search(j + 1))
                        break
                    else:
                        self.moveR(self.search(j + 1))
                        break
            i += 1
            print(self)

    def solve_recursive(self, disk: int):
        """solves the towers of hanoi using a recursive algorithm"""
        if disk == 0: return
        self.solve_recursive(disk - 1)
        if disk % 2 == 0:
            self.moveL(self.search(disk))
        else:
            self.moveR(self.search(disk))
        self.solve_recursive(disk - 1)
        print(self)
        self.status()


    def status(self) -> bool:
        """returns the status of the game, i.e. True if it is finished"""
        r1: int = 0
        r2: int = 0
        l: list[int] = [i for i in range(self.size, 0, -1)]
        for i in l:
            if i in self.tower_list[1]:
                r1 += 1
            if i in self.tower_list[2]:
                r2 += 1
        b: bool = ((r1 == self.size) or (r2 == self.size))
        if b:
            print("you've won!", end = " ")
            if self.count == (2**self.size - 1):
                print("and optimally at that!")
        return b

    def reset(self):
        """resets the towers of hanoi to their starting position"""
        self.__init__(self.size)

    def game(self):
        """play the towers of hanoi using user inputs"""
        while True:
            if self.status(): break
            a = int(input("move plate from tower: ")) - 1
            b = int(input("to tower: ")) - 1
            self.move(a, b)
            print(self)

if __name__ == "__main__":
    game: int = int(input("for recursive solver input 2, for iterative solver input 1, for user input 0: "))

    plates: int = int(input("number of plates: "))

    t = TowersOfHanoi(plates)
    print(t)

    match game:
        case 0:
            t.game()
        case 1:
            t.solve_iterative()            
        case 2:
            t.solve_recursive(plates)

