# Słownik polsko angielski
# polish_to_english = {
#     "amnezja": "amnesia",
#     "aktywista": "activist",
#     "burza": "storm"
# }
# print("Słownik polsko angielski:", polish_to_english)
# print(f"Po polsku 'burza' to po angielsku {polish_to_english['burza']}")

# Wartości mogą być róznych typw
# wydatki = {
#     "prąd": [250],
#     "woda": [40.34],
#     "zakupy": [
#     120.15,
#     30.85,
#     20.15
#     ]
# }
# print(wydatki)

# Typy int oraz float też moga byc kluczem
# wydatki = {
#     250: "prad",
#     30.45: "woda",
#     120.15: "zakupy",
#     170.3: "zakupy"
# }
# print(wydatki)

# Wartosci moga sie powtarzac w slowniku ale klucze nie
# wydatki = {
#     250: "prad",
#     30.45: "woda",
#     250: "zakupy"
# }
# print(wydatki)

# Słownik moga zawieraz inne slowniki
teacher = {
    "first_name": "Dominik",
    "last_name": "Wyszomirski",
    "age": "23",
    "contract": {
        "sign_date": "23-11-2018",
        "salary": 3500
    }
}
print(teacher)

# Podobnie jak w przypadku listy mozemy modyfikowac wartosc pod kluczem
# teacher["first_name"] = "Albert"
# print(teacher)

# Nowy klucz dodajemy w ten sam sposob (co nie zadziala w przypadku listy)
# teacher["city"] = "Gdansk"
# print(teacher)

# Cały klucz usuwamy tak samo jak w przypadku listy
# del teacher["last_name"]
# print(teacher)

# Metody słownia - wyciagniecie elementu po kluczu
# age = teacher.pop("age")
# print(age)
# print(teacher)

# Metody keys oraz values zwracaja obkiety specjalnych typow
# print(teacher.keys())
# print(teacher.values())

# Za pomoc funkcji lsit() mozmey zmienic te typy na liste kluczy i wartosci
# keys = list(teacher.keys())
# values = list(teacher.values())
# print(keys)
# print(values)

# Funkcja len na slowniku zwraca nam liczbe elementow (kluczy) w slowniku
# print(len(teacher))

# Tak jak slownik moze zawierac listy, tak lista moze zawierac slownik
# students = [
#     {
#         "first_name": "Dominik",
#         "last_name": "Wyszomirski"
#     },
#     {
#         "first_name": "Karola",
#         "last_name": "Styn"
#     }
# ]
# print(students)
# print(students[0])
# print(students[1])
# print(students[1]['first_name'])


