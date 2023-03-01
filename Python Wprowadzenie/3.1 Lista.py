# Lista smaków
ulubione_smaki = [
    "malinowy",     # 0 / -5
    "truskawkowy",  # 1 / -4
    "czekoladowy",  # 2 / -3
    "kokoswy",      # 3 / -2
    "pistacjowy",   # 4 / -1
]

# print("Ulubiony smak lodów:", ulubione_smaki[0])
# print("Drugi smak lodów:", ulubione_smaki[1])
# print("Trzeci smak lodów:", ulubione_smaki[2])
# print("Czwarty smak lodów:", ulubione_smaki[3])

# Długość listy
# print(f"Na liście jest {len(ulubione_smaki)} smaki lodów")

# Ostatni element listy
# print("Ostatni element:", ulubione_smaki[len(ulubione_smaki) -1])
# print("Dwa najbardziej ulubione smaki:", ulubione_smaki[:2])
# print("Wszystkie smaki poza dwoma ulubionymi:", ulubione_smaki[2:])
# print("Dwa najmniej ulubione smaki:", ulubione_smaki[-2:])

# Dodanie awaryjnego smaku na końcu listy
# print(ulubione_smaki)
# ulubione_smaki.append("kawowy")
# print(ulubione_smaki)

# Dodanie elementu w dowolnym miejscu
# ulubione_smaki.insert(2, "jagodowy")
# print(ulubione_smaki)

# Usuniecie elementu
# del ulubione_smaki[2]
# print(ulubione_smaki)

# Wyciągniecie z listy po indeksie
# drugi_smak = ulubione_smaki.pop(1)
# print(drugi_smak)
# print(ulubione_smaki)

# Usuniecie elementow po wartosci
# print(ulubione_smaki)
# ulubione_smaki.remove("czekoladowy")
# print(ulubione_smaki)

# Podmiana elementu
# print(ulubione_smaki)
# ulubione_smaki[-1] = "kawowy"
# print(ulubione_smaki)
#
#
name = "Dominik"

# Możemy odwołać się do konkretnego znaku w napisie za pomoca indeksu
# print("Pierwsza litera imienia to:", name[0])
# print("Ostatnia litera imienia to:", name[-1])
# print("Wszystkie litery poza pierwsza:", name[1:])

# Zmiana literki
# name = "K" + name[1:]
# print(name)

# Metoda split na stringu zwraca liste stringow
# words = "To jest całe zdanie".split(" ")
# print(words)
# print("To jest pierwsze słowo:", words[0])
