if __name__ == "__main__":
    year: int = int(input())

    if (year % 4 == 0) and not (year % 100 == 0) or (year % 400 == 0):
        print(f"Das Jahr {year} ist ein Schaltjahr")
    else:
        print(f"Das Jahr {year} ist kein Schaltjahr")