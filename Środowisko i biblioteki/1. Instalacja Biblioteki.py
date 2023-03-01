# alt + enter na bład i instalacja albo opcje Project/Python Interpreter
import geopy


def run_example():
    address = "Cechowa 47/4, 81-174 Gdynia"
    geolocator = geopy.Nominatim(user_agent="webinar-agent")
    address_code = geolocator.geocode(address)
    print(address_code.latitude)
    print(address_code.longitude)


if __name__ == "__main__":
    run_example()

# Wybor Biblioteki
# 1.Jaka jest wersja? (czy > niz 0.x)
# 2.Czytamy opis i dokumentacje(czy jest rozbudowana)
# 3.Jaka jest liczba pobran(czy ktos jej uzywa)
# 4.Kiedy byly ostatnie commity(czy ktos jeszcze ja rozwija)
# 5.Testujemy(jak dziala co chcemy wykorzystac)
# 6.Podejscie defensywne(abstrakcja i mozliwosc wymiany)
