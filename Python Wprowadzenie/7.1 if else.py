# Instrukcja warunkowa IF jest bardzo czytelna
# if 7 > 3:
#     print("To oczywsite!")
#
# if 10 < 4:
#     print("To sie nigdy nie zdarzy")

# If w polaczeniu z dynamiczynami (np. wprowadzoanami przez uzytkowanika) danami
# name = input("Jak sie nazywasz? ")
# print(f"Milo Cie poznac {name}")
#
# if len(name) >= 7:
#     print(f"{name} to całkiem dlugie imie!")
# else:
#     print(f"{name} to raczej krotkie imie!")


age = int(input("Ile masz lat?"))
if age < 18:
    print("Jeszcze nie mozesz glosowac")
else:
    print("Mozesz juz glosowac")
    if age >= 21:
        print("Mozesz kandydowac na posla")
    if age >= 30:
        print("Mozesz kandydowac na senatora")
    if age >= 35:
        print("Mozesz kandydowac na prezydenta")
