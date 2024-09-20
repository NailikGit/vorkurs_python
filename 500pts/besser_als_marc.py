import requests
from pprint import pprint
import os

def getAllTheCatsBreeds() -> list[dict]:
    """
        Holt eine Liste von Katzenrassen ab.
        Die Katzenrassen werden als Dictionaries empfangen.
        Todo: Erstelle Kadsenrassenklasse
    """
    baseurl: str = 'https://api.thecatapi.com/v1'
    antwort: requests.Response = requests.get(f'{baseurl}/breeds')
    return antwort.json()


def filterKadsen(kadsenrasse : dict, minimal_benötigtes_alter : int = 15) -> bool:
    """
        Nimmt eine Kadsenrasse entgegen und entscheidet,
        ob die Kadsenrasse für Marcs hohe Ansprüche geeignet ist.
        TODO: Was ist Schönheit?
    """

    # min_alter = int(kadsenrasse['life_span'].split(' ')[0])
    max_alter: int = int(kadsenrasse['life_span'].split(' ')[-1])

    # Der Marc möchte, dass seine Kadse mind. so alt werden kann
    # wie das minimal benötigte alter
    if max_alter >= minimal_benötigtes_alter:
        # TODO: Was ist eigentlich Schönheit?
        return True
    return False


def ladeKadsenRunter(kadsenrasse : dict):

    breed_id: str = kadsenrasse['id']
    kadsenurl: str = f'https://api.thecatapi.com/v1/images/search?limit=2&breed_ids={breed_id}&api_key= live_TGVJ51yKlCMZkAPe1G7soFWHPut1e0HmokGZiWnLn6Jszwi2Fk1sPBLDmeCMeVSN'
    antwort_der_webseite: list[dict] = requests.get(kadsenurl).json()

    links_zu_den_kadsen: list[str] = []
    for antwort in antwort_der_webseite:
        links_zu_den_kadsen.append(antwort['url'])

    for kadsen_url in links_zu_den_kadsen:
        # Datei Öffnen
        kadsen_dateiname: str = f"./images/{breed_id}_{kadsen_url.split('/')[-1]}"
        os.makedirs(os.path.dirname(kadsen_dateiname), exist_ok = True)
        if os.path.isfile(kadsen_dateiname): continue
        with open(kadsen_dateiname, "wb") as kadsen_datei:
            try:
                kadsen_daten: requests.Response = requests.get(kadsen_url)
                kadsen_datei.write(kadsen_daten.content)
                kadsen_datei.close()
            except:
                kadsen_datei.close()


def main1():
    kadsenrassen = getAllTheCatsBreeds()
    for kadsenrasse in kadsenrassen:
        if filterKadsen(kadsenrasse):
            # Die Kadsenrasse passt zu Marcs hohen Ansprüchen
            print(f"Rasse: {kadsenrasse['name']} Alter: {kadsenrasse['life_span']} BreedID: {kadsenrasse['id']}")
            try:
                ladeKadsenRunter(kadsenrasse)
            except:
                dnf.append(kadsenrasse)

def main2(l: list):
    for kadsenrasse in l:
        if filterKadsen(kadsenrasse):
            # Die Kadsenrasse passt zu Marcs hohen Ansprüchen
            print(f"Rasse: {kadsenrasse['name']} Alter: {kadsenrasse['life_span']} BreedID: {kadsenrasse['id']}")
            try:
                ladeKadsenRunter(kadsenrasse)
                dnf.remove(kadsenrasse)
            except:
                pass


if __name__ == '__main__':
    dnf: list = []
    main1()
    while dnf:
        main2(dnf)
