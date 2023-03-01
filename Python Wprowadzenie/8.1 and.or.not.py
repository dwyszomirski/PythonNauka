# 1 Warunek AND
# name = input("Jak sie nazywasz? ")
# print(f"Miło Cie poznac {name}")
# name_lenght = len(name)
#
# if name_lenght < 5:
#     print(f"{name} to raczej krotkie imie")
# else:
#     if 5 <= name_lenght <= 8:
#         print(f"{name} to imie zwyklej dlugosci!")
#     else:
#         print(f"{name} to dlugie imie!")

# 2 Warunek AND
# born_as_usa_citizen_answer = input("Czy jestes obywatelem USA od urodzenia T/N ")
# age = int(input("Ile masz lat? "))
# usa_residence_years = int(input("Ile lat mieszkasz w USA? "))
#
# if born_as_usa_citizen_answer == "T":
#     born_as_usa_citizen_answer = True
# else:
#     born_as_usa_citizen_answer = False
#
# if born_as_usa_citizen_answer and age >= 35 and usa_residence_years >= 14:
#     print("Mozesz kandydowac")
# else:
#     print("Nie mozesz kandydowac")

# 3 Warunek OR
# income = float(input("Jaki jest miesieczny przychod Twojej firmy? "))
# number_of_empolyers = int(input("Ilu pracownikow zatrudniasz? "))
#
# if income < 15500 or number_of_empolyers >= 3:
#     print("Mozesz otrzymac dotacje")
# else:
#     print("Nie otrzymasz dotacji")

# operator and i or
# if income < 15500 or (number_of_empolyers >= 3 and income < 30000):
#     print("Mozesz otrzymac dotacje!")
# else:
#     print("Niestety nie otrzymasz dotacji")

# 4 Warunek NOT
income = float(input("Jaki jest miesieczny przychod Twojej firmy? "))
number_of_empolyers = int(input("Ilu pracownikow zatrudniasz? "))
support_answer = input("Czy Twoja firma otrzymala juz jakies wsparcie? (T/N) ")

if support_answer == "T":
    support_used = True
else:
    support_used = False

if not support_used and (income < 15500 or number_of_empolyers >= 3):
    print("Mozesz otrzymac dotacje")
else:
    print("Niestety nie otrzymasz dotacji!")