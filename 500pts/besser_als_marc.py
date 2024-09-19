import requests
from pprint import pprint

def getAllTheCatsBreeds() -> list[dict]:
    """
        Holt eine Liste von Katzenrassen ab.
        Die Katzenrassen werden als Dictionaries empfangen.
        Todo: Erstelle Kadsenrassenklasse
    """
    baseurl = 'https://api.thecatapi.com/v1'
    antwort = requests.get(f'{baseurl}/breeds')
    return antwort.json()


def filterKadsen(kadsenrasse : dict, minimal_benötigtes_alter : int = 15) -> bool:
    """
        Nimmt eine Kadsenrasse entgegen und entscheidet,
        ob die Kadsenrasse für Marcs hohe Ansprüche geeignet ist.
        TODO: Was ist Schönheit?
    """

    # min_alter = int(kadsenrasse['life_span'].split(' ')[0])
    max_alter = int(kadsenrasse['life_span'].split(' ')[-1])

    # Der Marc möchte, dass seine Kadse mind. so alt werden kann
    # wie das minimal benötigte alter
    if max_alter > minimal_benötigtes_alter:
        # TODO: Was ist eigentlich Schönheit?
        return True
    else:
        return False


def ladeKadsenRunter(kadsenrasse : dict):

    breed_id = kadsenrasse['id']
    kadsenurl = f'https://api.thecatapi.com/v1/images/search?limit=2&breed_ids={breed_id}&api_key=REPLACE_ME'
    antwort_der_webseite = requests.get(kadsenurl).json()

    links_zu_den_kadsen = []
    for antwort in antwort_der_webseite:
        links_zu_den_kadsen.append(antwort['url'])

    for kadsen_url in links_zu_den_kadsen:
        # Datei Öffnen
        kadsen_dateiname = f"./images/{breed_id}_{kadsen_url.split('/')[-1]}"
        kadsen_datei = open(kadsen_dateiname, 'wb')
        kadsen_daten = requests.get(kadsen_url)
        kadsen_datei.write(kadsen_daten.content)
        kadsen_datei.close()


def main():
    kadsenrassen = getAllTheCatsBreeds()
    for kadsenrasse in kadsenrassen:
        if filterKadsen(kadsenrasse):
            # Die Kadsenrasse passt zu Marcs hohen Ansprüchen
            print(f"Rasse: {kadsenrasse['name']} Alter: {kadsenrasse['life_span']} BreedID: {kadsenrasse['id']}")
            ladeKadsenRunter(kadsenrasse)

if __name__ == '__main__':
    main()
