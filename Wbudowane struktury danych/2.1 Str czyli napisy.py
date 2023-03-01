def run_example():
    # Metoda join stosuje podany string jako łacznik do scalenia listy napisow w jeden
    account_number_parts = ["1234", "4576", "8910", "3214", "7840"]
    print("-".join(account_number_parts))
    # Pusty napis tez moze byc łącznikiem
    print("".join(account_number_parts))

    # Metody lstrip, rstrip oraz strip usuwaja znaki odpowiednio z lewej, prawej i obu stron napisu
    name = "   Dominik   "
    left_clear = name.lstrip()
    right_clear = name.rstrip()
    both_clear = name.strip()
    print(f"{left_clear} Wyszomirski")
    print(f"{right_clear} Wyszomirski")
    print(f"{both_clear} Wyszomirski")

    # Każda z tych metod przyjmuje tez ciag znakow - jezeli znajdzie ktorykolwiek z nich usuwa itd.
    # Domyslnie usuwa dostep
    name2 = " -|  Dominik  |- "
    left_clear2 = name2.strip("-| ")
    right_clear2 = name2.rstrip("-| ")
    both_clear2 = name2.strip("-| ")
    print(f"{left_clear2} Wyszomirski")
    print(f"{right_clear2} Wyszomirski")
    print(f"{both_clear2} Wyszomirski")

    # Metody startswith sprawdzaja czy dany napis odpowiednio zaczyna i konczy sie prefixem/suffixem
    # Opcjonalne argumenty pozwalaja podac inny niz poczatek/koniec napisu zakresu wyszukiwania
    last_name = "Wyszomirski"
    print(last_name.startswith("Wys"))
    print(last_name.startswith("Kow"))
    print(last_name.endswith("ski"))
    print(last_name.endswith("ak"))

    # Metoda zfill "dopełnia" napis zerami do osiagniecia podanej długosci.
    # jest to przydatne np. do budowania id o okreslonym formacie
    number = 135
    id = str(number).zfill(8)
    print(id)

    # Metody find oraz index pozwalaja pierwszy indeks pod ktorym wystepuje ciag znakow w napisie
    sentence = "Ale dzisiaj ładny dzień! Wczoraj tez był dobry dzień."
    print(sentence.find("dzień"))
    print(sentence.index("dzień"))

    # Opcjonalne argumenty pozwalaja podan inny zakres wyszukiwania
    # wyszukiwanie w czesci napisu [start:end] - domyslnie poczatek do konca
    print(sentence.find("dzień", 20))
    print(sentence.index("dzień", 24))

    # Index dziala tak samo jak find, przy czym jezeli ciag znakow nie zostanie znaleziony
    # find zwraca -1 a index rzuca bład
    print(sentence.find("Tego tam nie ma"))
    # print(sentence.index("Tego tam nie ma"))


if __name__ == "__main__":
    run_example()
