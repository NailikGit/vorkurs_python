import requests

def wikipedia_game(begin: str, end: str) -> list[str]:
    req: str = begin

    path: list[str] = [begin]

    while not req == end:
        r: requests.Response = requests.get(f"https://de.wikipedia.org/w/api.php?action=query&prop=links&pllimit=max&format=json&titles={req}")
        d: dict = r.json()
        l: list[dict[str, str]] = d["query"]["pages"][list(d["query"]["pages"].keys())[0]]["links"]

        counter: int = 0
        for a in l:
            print(f"{counter}: {a["title"]}")
            counter += 1

        user: int = int(input("continue to index: "))

        req: str = l[user]["title"]

        path.append(req)

    return path


if __name__ == "__main__":
    begin: str = input("Startartikel: ")
    end: str = input("Endartikel: ")
    
    path: list[str] = wikipedia_game(begin, end)

    print(f"path taken: {path}")
