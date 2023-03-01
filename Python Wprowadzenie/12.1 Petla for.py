# collection = ["ciastko", "ksiazka", "piłka"]
# for element in collection:
#     print(element)

# Wypisywanie listy ulubionych sportow
# favourite_sports = ["bieganie", "pływanie", "jazda na rowerze"]
# for sport in favourite_sports:
#     print(sport)

 # Za pomoc petli for mozemy wypisac klucze ze słownika
# expenditure = {
#      "prad": [250],
#      "woda": [30.45],
#      "zakupy": [
#          120.15,
#          170.32,
#          2.15
#     ]
# }
# for expenditures_name in expenditure:
#      print(expenditures_name)

# Klucze i wartosci
# for expenditures_name in expenditure:
#     print(f"{expenditures_name} -> {expenditure[expenditures_name]}")

# Same wartosci
# for wydatki in expenditure.values():
#     print(expenditure)

# Klucze i wartosci bezposrednio
# for expenditures_name, expenditure in expenditure.items():
#     print(f"{expenditures_name} -> {expenditure}")

# Krotke mozna "rozpakowac"
# item = ("prad", 340)
# name, value = item
# print(name, value)

# Wypisujemy kod pocztowy - znak po znaku z informacja o kolejnosci
# post_code = input("Jaki jest Twoj kod pocztowy? ")
# for index, letter in enumerate(post_code):
#     print(f"[{index}] -> {letter}")

# Wypisywanie co drugiego sportu
# favourite_sports = ["bieganie", "pływanie", "jazda na rowerze", "dupa"]
# for index, sport in enumerate(favourite_sports):
#     if index % 2 == 0:
#         print(sport)

# Zamieniamy kod pocztowy by zawsze byl zgodny z formate xx-xx-xx..
post_code = input("Jaki jest Twoj kod pocztowy? ")
post_code = post_code.replace("-", "")
formatted_post_code = ""
for index, letter in enumerate(post_code):
    if index % 2 == 0 and index != 0:
        formatted_post_code += "-"
    formatted_post_code += letter
print(formatted_post_code)