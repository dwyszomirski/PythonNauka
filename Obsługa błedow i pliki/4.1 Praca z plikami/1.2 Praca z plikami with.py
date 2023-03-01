#TODO Sciezka wzgeldna i bezwzgledna
# Sciezka wzgledna(relatywna): katalog/plik.txt         some_directory/other_file.txt
# Sciezka bezwzgledna(absolutna): C:\katalog\plik.txt   some_directory\\other_file.txt
# Funkcja os.path.join("some_directory", "other_file.txt")


def run_example():
    path_of_file = "plain_text.txt"

    try:
        with open(path_of_file, mode="r") as plain_text_file:
            text_data = plain_text_file.read()
    except IOError:
        print("Nie udalo sie wczytac danych...")
    else:
        print("Dane z pliku...")
        print(text_data)

    print("Do zobaczenia pozniej")


if __name__ == "__main__":
    run_example()
