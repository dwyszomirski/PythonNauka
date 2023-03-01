def run_example():
    # W przykladach ze słownikiem posłuzymy sie słowinikiem wydatkow
    expenditures = {
        "prad": [250],
        "woda": [30.34],
        "zakupy": [
            120.14,
            170.53,
            20.15
        ]
    }
    print(expenditures)

    # Metoda clear usuwa wszystkie elementy ze słownika
    # expenditures.clear()
    print(expenditures)

    # Metoda copy tworzy i zwraca kopie słownika
    expenditures_copy = expenditures.copy()
    # expenditures.clear()
    print(expenditures)
    print(expenditures_copy)

    # Za pomoca metody get mozemy otrzymac wartosc, ktora jest pod danym kluczem
    # Nie powoduje to "wyjecia" elementu ze słownika - dalej tam jest
    water_expenditures = expenditures.get("woda")
    print(water_expenditures)
    print(expenditures)

    # Get w przeciwienstwie do odwłoania bezposrednio po kluczu nie zwraca błedu tylko None gdy nie znajdzie klucza
    cookies_expenditures = expenditures.get("ciasteczka")
    print(cookies_expenditures)

    # Drugi, opcjonalny arugment pozwala podac wartosc, ktora zostanie zwrocona gdy dany klucz nie wystepuje w slowniku
    cookies_expenditures = expenditures.get("ciasteczka", [10])
    print(cookies_expenditures)

    # Za pomoca metody update mozemy zaktualizowac słownik o nowe klucze.
    # Nazwa argumentu zostanie uzyta jako klucz
    expenditures.update(jedzenie=[120], rozrywka=[70])
    print(expenditures)

    # Jezeli klucz sie powtarza zostanie on nadpisany
    expenditures.update(woda=[95])
    print(expenditures)

    # Do metody update mozna tez przekazac inny słownik
    other_expenditures = {
        "remont": [1450],
        "internet": [50]
    }
    expenditures.update(other_expenditures)
    print(expenditures)


if __name__ == "__main__":
    run_example()