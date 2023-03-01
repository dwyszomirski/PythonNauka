# Zmieniamy numer telefonu tak by sie zgadzal z formatem xxx-xxx-xxx
# phone_number = input("Jaki jest Twoj numer telefonu? ")
# phone_number = phone_number.replace("-", "")
# fbormatted_phone_numer = ""
# letter_index = 0
# while letter_index < len(phone_number):
#     if letter_index % 3 == 0 and letter_index != 0:
#         formatted_phone_number += "-"
#     formatted_phone_number += phone_number[letter_index]
#     letter_index += 1
# print(formatted_phone_number)

# Pytaj uzytkownika o liczbe tak dlugo az poda parzysta albo przekroczy limit 10 prob
# number = int(input("Podaj liczbe parzysta: "))
# try_number = 1
# while try_number < 10 and number % 2 != 0:
#     number = int(input("Sprobuj jeszcze raz. Podaj liczbe parzysta: "))
#     try_number += 1

# Popros uzytkownika o podanie ulubionych dan, rozdzielajac kazde z nich przecinkiem.
dishes = input("Podaj swoje ulubione danie, rozdzielajac je przecinkiem: ")
favourite_dishes = dishes.split(",")
dish_index = 0
while dish_index < len(favourite_dishes):
    print(f"Ulubione danie numer {dish_index}: {favourite_dishes[dish_index]}")
    dish_index += 1