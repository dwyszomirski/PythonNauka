# Dopoki licznik nie przekroczy 30 wypisujemy kolejne liczby
# conuter = 0
# while conuter <= 30:
#     print(conuter)
#     conuter += 1

# expected_potatoes = int(input("Ile ziemniakow chcesz na obiad? "))
# potatoes = []
# while len(potatoes) < expected_potatoes:
#     print("Obieram ziemniaka..")
#     print("I wrzucam go do garnka.")
#     potatoes.append("Ziemniak")
# print(potatoes)

# Chcemy zeby liczba podana przez uzytkownika byla wieksza niz 100
# number = 0
# while number <= 100:
#     number = int(input("Podaj liczbe wieksza niz 100: "))
#     if number <= 100:
#         print(f"{number} nie jest wieksze niz 100! Sprobujmy jeszcze raz... \n")
#
# print(f"Brawo!")

# Mozemy upewnic sie, ze uzytykownik podal sensowna wartosc
# age = int(input("Ile masz lat? "))
# while age < 1:
#     print("Chyba nie...\n")
#     age = int(input("Ile masz lat? "))
#
# if age < 18:
#     print("Jeszcze nie mozesz glosowac")
# else:
#     print("Mozesz juz glosowac")

# Wypisujemy kod pocztowy - znak po znaku
# post_code = input("Jaki jest Twoj kod pocztowy? ")
# letter_index = 0
# while letter_index < len(post_code):
#     print(f"{letter_index} -> {post_code[letter_index]}")
#     letter_index += 1


# Zmieniamy kod pocztowy by zawsze byl zgodny z formatem xx-xx-xx
# post_code = input("Jaki jest Twoj kod pocztowy? ")
# post_code = post_code.replace("-", "")
# formatted_post_code = ""
# letter_index = 0
# while letter_index < len(post_code):
#     if letter_index % 2 == 0 and letter_index != 0:
#         formatted_post_code += "-"
#     formatted_post_code += post_code[letter_index]
#     letter_index += 1
# print(formatted_post_code)