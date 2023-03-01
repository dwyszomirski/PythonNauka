# Poszukiwanie elementu w zbiorze
expenditures = [120, 300, 250.45, 600, 50]

# for expenditure in expenditures:
#     # print(expenditure)
#     if expenditure > 1000:
#         print("Drogi wydatek znaleziony!")
#         break

# Petla for posiada rowniez opcjonalna czesc "else"
# for expenditure in expenditures:
#     if expenditure > 1000:
#         print("Drogi wydatek znaleziony")
#         break
# else:
#     print("Nie znaleziono nic super drogiego")

# Break do przerwania wprowadzenia informacjii od uzytkowanika
grades = []
while True:
    grade_input = input("Podaj kolejna ocene albo zakoncz wpisujac 'X': ")
    if grade_input == "X":
        break
    grade = int(grade_input)
    grades.append(grade)

grades_sum = sum(grades)
average = grades_sum / len(grades)
print(f"Twoja srednia wynosi: {average:.2f}")

# Rowniez petla while ma opcjonalnego "else"
grades = []
while len(grades) < 5:
    grade_input = input("Podaj kolejna ocene albo zakoncz wpisujac 'X': ")
    if grade_input == "X":
        break
    grade = int(grade_input)
    grades.append(grade)
else:
    print("Wystarczy tych ocen")

grades_sum = sum(grades)
average = grades_sum / len(grades)
print(f"Twoja srednia wynosi: {average:.2f}")

# Wypisywanie co drugiego sportu
favourite_sports = ["bieganie", "pływanie", "jazda na rowerze", "piłka nozna"]
for index, sport in enumerate(favourite_sports):
    if index % 2 != 0:
        continue
    print(sport)
