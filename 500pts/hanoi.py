import time

class TowersOfHanoi():
    """class that models the towers of hanoi game including iterative solver"""
    global aosf
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
        r: str = ""
        for i in range(self.size - 1, -1, -1):
            for j in self.tower_list:
                se: str = ""
                sb: str = ""
                try:
                    if j[i]:
                        if j[i] > 9:
                            sb = (self.size - j[i]) * " " + (j[i] - 1) * "-"
                        else:
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
        try:
            if origin < 0 or origin > 2: raise Exception(f"tower {origin} doesn't exist")
            if to < 0 or to > 2: raise Exception(f"tower {to} doesn't exist")
        except Exception:
            print(Exception)
            return

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

    def forceMove(self, origin: int, to : int):
        """moves the uppermost plate from tower 'origin' to tower 'to' without checking legal moves"""
        self.tower_list[to].append(self.tower_list[origin].pop)
        self.counter += 1

    def search(self, n: int) -> int:
        """(deprecated) returns the number of the tower, that contains 'n', defaults to -1, if 'n' doesn't exist"""
        for i in range(0, 3):
            if(self.tower_list[i]):
                top: int = self.tower_list[i].pop()
                self.tower_list[i].append(top)
                if top == n:
                    return i
        return -1

    def moveR(self, origin: int):
        """(deprecated) moves element from 'origin' one tower to the right (with wrapping)"""
        self.forceMove(origin, (origin + 1) % 3)

    def moveL(self, origin: int):
        """(deprecated) moves element from 'origin' one tower to the left (with wrapping)"""
        self.forceMove(origin, (origin + 2) % 3)

    def _solve_iterative_old(self):
        """(deprecated) solves the towers of hanoi using an iterative algorithm"""
        while not self.status():
            for j in range(0, self.size):
                if ((self.count + 1) & 2**j):
                    if j % 2 == 0:
                        self.moveL(self.search(j + 1))
                        break
                    else:
                        self.moveR(self.search(j + 1))
                        break

            #print("\x1b[F" * self.size, end = "")
            #print(self, end = "")

    def _solve_iterative_with_search(self):
        """(deprecated) solves the towers of hanoi using an iterative algorithm"""
        while not self.status():
            xor = self.count ^ (self.count + 1)
            plate = xor.bit_count()
            if (plate % 2) == 0:
                self.moveL(self.search(plate))
            else:
                self.moveR(self.search(plate))

            #print("\x1b[F" * self.size, end = "")
            #print(self, end = "")

    def solve_iterative(self):
        """solves the towers of hanoi using an iterative algorithm"""
        while not self.status():
            xor = self.count ^ (self.count + 1)
            plate = xor.bit_count()
            move_direction = (plate % 2) == 0
            move_from = (self.count >> (plate - int(move_direction))) % 3

            self.forceMove(move_from, (move_from + move_direction + 1) % 3)

            #print(f"\x1b[{self.size}F", end = "")
            #print(self, end = "")

    def _solve_recursive_with_search(self, plate: int):
        """(deprecated) solves the towers of hanoi using a recursive algorithm"""
        if plate == 0: return
        self.solve_recursive(plate - 1)
        if plate % 2 == 0:
            self.moveL(self.search(plate))
        else:
            self.moveR(self.search(plate))

        print("\x1b[F" * self.size, end = "")
        print(self, end = "")

        self.solve_recursive(plate - 1)

    def solve_recursive(self, plate: int):
        """solves the towers of hanoi using a recursive algorithm"""
        if plate == 0: return
        self.solve_recursive(plate - 1)
        if plate % 2 == 0:
            self.moveL((self.count >> (plate - 1)) % 3)
        else:
            self.moveR((self.count >> plate) % 3)

        print("\x1b[F" * self.size, end = "")
        print(self, end = "")
        
        self.solve_recursive(plate - 1)


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
            print(f"\x1b[{self.count}F", end = "")
            print(self, end = "")

    def end(self):
        if self.status():
            print("you've won", end = "")
            if self.count == ((1 << self.size) - 1):
                print(" and optimally at that", end = "")
        print("!")

if __name__ == "__main__":
    game: int = int(input("for recursive solver input 2, for iterative solver input 1, for user input 0: "))

    plates: int = int(input("number of plates: "))

    t = TowersOfHanoi(plates)
    print(t, end = "")

    match game:
        case 0:
            t.game()
        case 1:
            t.solve_iterative()
            print(t)
        case 2:
            t.solve_recursive(plates)
        case 3:
            ostart = time.perf_counter()
            t.solve_iterative_old()
            oend = time.perf_counter() - ostart
            o = f"unoptimized took:           {oend}s"

            t.reset()

            wsstart = time.perf_counter()
            t.solve_iterative_with_search()
            wsend = time.perf_counter() - wsstart
            ws = f"optimized with search took: {wsend}s"

            t.reset()

            nstart = time.perf_counter()
            t.solve_iterative_with_search()
            nend = time.perf_counter() - nstart
            n = f"fully optimized took:       {nend}s"

            print(f"\x1b[{t.size}F", end = "")
            print(t)
            t.end()
            print(o + "\n" + ws + "\n" + n)