# 1
# apple_price = float(input("Ile kosztuja jabłka? "))
# orange_price = float(input("Ile kosztuja pomarancze? "))
# potato_price = float(input("Ile kosztuja ziemniaki? "))
#
# if apple_price > orange_price:
#     print("Jabłka sa drozsze od pomaraczny")
# else:
#     print("Pomarancze sa drozsze od jabłek")
#
# if potato_price > apple_price:
#     print("Ziemniaki sa drozsze od jablek")
# else:
#     print("Jablka sa drosze od ziemniakow")

# produkty = input("Wprowadz liste zakupow, rozdzielajac poszczegolne elementy przecinkiem ")
# lista_produktow = produkty.split(",")
# if len(lista_produktow) > 4:
#     print("Uwazam ze Twoja lista zakupow jest dluga")
# else:
#     print("Uwazam ze Towja lista zakupow jest krotka")

# 2
# print("Ile miesiecznie wydajesz na")
# food = float(input("jedzenie? "))
# fun = float(input("rozrywke? "))
# bills = float(input("oplaty? "))
# other = float(input("inne? "))
#
# total_sum = food + fun + bills + other
# total_sum_procentage = {
#     "jedzenie": food * 100 / total_sum,
#     "rozrywka": fun * 100 / total_sum,
#     "oplaty": bills * 100 / total_sum,
#     "inne": other * 100 / total_sum,
# }
# most_important_category = "jedzenie"
# if total_sum_procentage["rozrywka"] > total_sum_procentage[most_important_category]:
#     most_important_category = "rozrywka"
# if total_sum_procentage["oplaty"] > total_sum_procentage[most_important_category]:
#     most_important_category = "oplaty"
# if total_sum_procentage["inne"] > total_sum_procentage[most_important_category]:
#     most_important_category = "inne"
#
# print(f"Najwiecej wydajesz na {most_important_category} - {total_sum_procentage[most_important_category]:.0f}%")

# 3
# math_ocena = int(input("Jaka jest Twoja ocena koncowa z matematyki? "))
# fizyka_ocena = int(input("Jaka jest Twoja ocena koncowa z fizyki? "))
# polski_ocena = int(input("Jaka jest Twoja ocena koncowa z polskiego? "))
# angielski_ocena = int(input("Jaka jest Twoja ocena koncowa z angielskiego? "))
# historia_ocena = int(input("Jaka jest Twoja ocena koncowa z historii? "))
#
# number_of_failures = 0
#
# if math_ocena < 2:
#     number_of_failures = number_of_failures + 1
#
# if fizyka_ocena < 2:
#     number_of_failures = number_of_failures + 1
#
# if polski_ocena < 2:
#     number_of_failures = number_of_failures + 1
#
# if angielski_ocena < 2:
#     number_of_failures = number_of_failures + 1
#
# if historia_ocena < 2:
#     number_of_failures = number_of_failures + 1
#
# if number_of_failures == 0:
#     print("Gratulacje! Zdales/Zdalas do nastepnej klasy :) ")
# else:
#
#     if number_of_failures == 1:
#         srednia = (math_ocena + fizyka_ocena + polski_ocena + angielski_ocena + historia_ocena) / 5
#         if srednia >= 3.4:
#             print("Gratulacje! Zdales/Zdalas do nastepnej klasy :) ")
#         else:
#             print("Niestety...")
#     else:
#         print("Niestety...")

# 4

# name = input("Jak masz na imie? ")
# if name[-1] == "a":
#     print("Jestes kobieta")
# else:
#     print("Jestes mezczyzna")
