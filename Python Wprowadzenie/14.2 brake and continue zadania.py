# zadanie 1
# subjects = ["matematyka", "fizyka", "jezyk polski", "jezyk angielski", "historia"]
# grades = []
# for subject in subjects:
#     grade = int(input(f"Jaka jest Twoja ocena koncowa z przedmiotu {subject}? "))
#     grades.append(grade)
#
# for grade in grades:
#     if grade == 1:
#         print("Niestety...")
#         break
#
# else:
#     print("Gratulacje! Zdales/zdalas do nastepnej klasy :)")

# zadanie 3
numbers = [1, 3, 4, 2, 3, 4, 56, 234, 2, 5231, 54, 62, 523, 451, 34]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)


