if __name__ == "__main__":
    # d = {}
    s: str = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
    """ s = list(s)
        for i in s:
            if i == " ":
                continue
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1"""

    d: dict[chr, int] = {ch:s.count(ch) for ch in s if ch != " "}

    print(d)
