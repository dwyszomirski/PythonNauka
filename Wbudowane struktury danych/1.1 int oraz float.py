import math
import random


def run_example():
    # Zaokrąglenie za pomoca wbudowanej funkcji round - do najblizszej liczby całkowitej
    print(round(2.7))

    # Jezeli dwie liczby sa rownie blisko to zaokragla do parzystej
    print(round(1.5))
    print(round(2.5))

    # Opcjonalny argument ngdigits pozwala podac do jakiego miejsca zaokraglamy
    print(round(3.129, ndigits=2))

    # Funkcja floor zwraca najwieszka liczbe całkowita, ktora jest mniniejsza od podanej
    print(math.floor(3.9))
    print(math.floor(1.1))
    print(math.floor(-1.1))

    # Funkcja ceil zwraca najwieksza liczbe całkowita, ktora jest mniejsza od podanej
    print(math.ceil(3.9))
    print(math.ceil(1.1))
    print(math.ceil(-1.1))

    # Najprostszy sposobem na podniesienie liczby do potegi jest uzycie operatora
    print(2 ** 5)

    # Funkcja wbudowana pow dziala analogicznie
    print(pow(2, 10))

    # Jej dodatkowy argument pozwala na zwrocenie wartosci modulo z potegowania
    print(pow(2, 10, mod=10))

    # Funckja pow z modulu math dziala analogicznie, przy czym zawsze zamienia wartosci na float
    print(math.pow(2, 8))

    # Funkcja randiant losuje liczby całkowita z podanego przedzialu
    # W rzeczywistosci liczby generowane przez random sa pseudlosowe
    print(random.randint(5, 10))

    # Uniform dziala analogicznie dla warosci float
    print(random.uniform(-10, 20))

if __name__ == "__main__":
    run_example()