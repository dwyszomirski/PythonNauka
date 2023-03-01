# TODO
# TODO read() -> Przeczytaj cały plik
# TODO read(wartosc) -> Przeczytaj wartosc bajtow
# TODO readline() -> Przeczytaj nastepna linie
# TODO readlines() -> Przeczytaj wszystkie linie
# TODO write(<tresc>) -> Zapisz tresc do pliku

def run_example():
    with open("plain_text.txt", mode="r") as plain_text_file:
        print(plain_text_file.read(25))
        print(plain_text_file.read(25))

        line = plain_text_file.readline()
        while line:
            print(f"Kolejna linia tekstu: {line}")
            line = plain_text_file.readline()

    with open("plain_text.txt", mode="r") as plain_text2_file:
        lines = plain_text2_file.readlines()
    for line_number, line in enumerate(lines):
        print(f"{line_number} {line}")


if __name__ == "__main__":
    run_example()