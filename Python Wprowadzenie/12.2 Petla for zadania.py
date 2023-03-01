# Zadanie 1
# oceny = []
# ocena_input = input("Podaj kolejna ocene albo zakoncz wpisujac 'X': ")
# while ocena_input != 'X':
#     ocena = int(ocena_input)
#     oceny.append(ocena)
#     ocena_input = input("Podaj kolejna ocene albo zakoncz wpisujac 'X': ")
#
# suma_ocen = 0
# for ocena in oceny:
#     suma_ocen += ocena
# srednia = suma_ocen / len(oceny)
# print(f"Twoja srednia wynosi: {srednia: .2f}")

# Alternatywa
# suma_ocen = sum(oceny)

# Zadanie 2
# phone_number = input("Jaki jest Twoj numer telefonu? ")
# phone_number = phone_number.replace("-", "")
# formatted_phone_number = ""
# for index, letter in enumerate(phone_number):
#     if index % 3 == 0 and index != 0:
#         formatted_phone_number += "-"
#     formatted_phone_number += letter
# print(formatted_phone_number)

# Zadanie 3
# print("Kalkulator budzetu miesiecznego")
# wydatki = {}
#
# category_name = input("Podaj kategorie wydatkow albo zakoncz wpisujac 'X': ")
# while category_name != 'X':
#     wydatki[category_name] = []
#     wydatek = input(f"Podaj wartosc nastepnego wydatku w kategorii {category_name} albo zakoncz 'X': ")
#     while wydatek != 'X':
#         wydatek_wartosc = float(wydatek)
#         wydatki[category_name].append(wydatek_wartosc)
#         wydatek = input(f"Podaj wartosc nastepnego wydatku w kategorii {category_name} albo zakoncz 'X': ")
#     category_name = input("Podaj kategorie wydatkow albo zakoncz wpisujac 'X': ")
#
# wszystkie_wydatki = 0
# for kategoria_wydatkow in wydatki.values():
#     wszystkie_wydatki += sum(kategoria_wydatkow)
#
# procent_wydatkow = {}
# for category_name, kategoria_wydatkow in wydatki.items():
#     cala_kategoria_wydatkow = sum(kategoria_wydatkow)
#     procent_wydatkow[category_name] = cala_kategoria_wydatkow * 100 / kategoria_wydatkow
#
# most_important_category = None
# most_important_category_percentage = 0
# for kategorii, procent in procent_wydatkow.items():
#     if procent > most_important_category_percentage:
#         most_important_category_percentage = procent
#         most_important_category = kategorii
#
# if most_important_category is not None:
#     print(f"Najwiecej wydajesz na {most_important_category} - {most_important_category_percentage}")
#
# for kategorii, procent in procent_wydatkow.items():
#     print(f"Na {kategorii} wydajesz {procent:.0f}% miesiecznych wydatkow")


print("Kalkulator budzetu miesiecznego")
expenditures = {}

category_name = input("Podaj kategorie wydatkow albo zakoncz wpisujac 'X': ")
while category_name != 'X':
    expenditures[category_name] = []
    expenditure = input(f"Podaj wartosc nastepnego wydatku w kategorii {category_name} albo zakoncz 'X': ")
    while expenditure != 'X':
        expenditure_value = float(expenditure)
        expenditures[category_name].append(expenditure_value)
        expenditure = input(f"Podaj wartosc nastepnego wydatku w kategorii {category_name} albo zakoncz 'X': ")
    category_name = input("Podaj kategorie wydatkow albo zakoncz 'X': ")

total_expenditures = 0
for category_expenditures in expenditures.values():
    total_expenditures += sum(category_expenditures)

expenditures_precentage = {}
for category_name, category_expenditures in expenditures.items():
    total_category_expenditures = sum(category_expenditures)
    expenditures_precentage[category_name] = total_category_expenditures * 100 / total_category_expenditures

most_important_category = None
most_important_category_precentage = 0
for category, precentage in expenditures_precentage.items():
    if precentage > most_important_category_precentage:
        most_important_category_precentage = precentage
        most_important_category = category

if most_important_category is not None:
    print(f"Najwiecej wydajesz na {most_important_category} - {most_important_category_precentage}")

for category, precentage in expenditures_precentage.items():
    print(f"Na {category} wydajesz {precentage:.0f}% miesiecznych wydatkow")