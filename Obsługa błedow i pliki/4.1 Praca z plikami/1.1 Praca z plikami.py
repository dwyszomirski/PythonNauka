def run_example():
    path_of_file = "plain_text.txt"

    try:
        plain_text_file = open(path_of_file, mode="r")  # https://docs.python.org/3/library/functions.html#open
        try:
            print("Wczytujemy dane")
            # raise IOError
            text_data = plain_text_file.read()
        finally:
            print("Zamykamy plik")
            plain_text_file.close()
    except IOError:
        print("Nie udalo sie wczytac danych...")
    else:
        print("Dane z pliku:")
        print(text_data)

    print("Do zobaczenia pozniej!")


if __name__ == "__main__":
    run_example()