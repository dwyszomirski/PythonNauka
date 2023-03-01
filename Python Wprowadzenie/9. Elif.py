# Instrukcja ELIF pozwala powiedziec "inaczej, jesli..."
# income = 5000
# employees_number = 7
# years_on_the_market = 3
#
# if income < 5000:
#     print("Przyznano głowne wsparcie")
# elif 5 <= employees_number <= 10:
#     print("Przyznano wsparcie z funduszu prackownikow")
# elif years_on_the_market < 3:
#     print("Przyznano wsparcie dla nowych firm")
# else:
#     print("Przyznano wsparcie na pocieszenie :)")


# Zadanie test coopera
wiek = int(input("Ile masz lat? "))
plec = input("Jaka masz plec K/M ? ")
uzyskany_wynik = int(input("Jaki masz wynik? "))

if wiek == 8:
    if plec == "M":
        if uzyskany_wynik >= 2190:
            print("Bardzo dobrze")
        elif uzyskany_wynik >= 1810:
            print("Dobrze")
        elif uzyskany_wynik >= 1420:
            print("Srednio")
        elif uzyskany_wynik >= 1050:
            print("Zle")
        else:
            print("Bardzo zle")
    else:
        if uzyskany_wynik >= 2010:
            print("Bardzo dobrze")
        elif uzyskany_wynik >= 1670:
            print("Dobrze")
        elif uzyskany_wynik >= 1320:
            print("Srednio")
        elif uzyskany_wynik >= 990:
            print("Zle")
        else:
            print("Bardzo zle")
elif wiek == 9:
    if plec == "M":
        if uzyskany_wynik >= 2350:
            print("Bardzo dobrze")
        elif uzyskany_wynik >= 1950:
            print("Dobrze")
        elif uzyskany_wynik >= 1540:
            print("Srednio")
        elif uzyskany_wynik >= 1130:
            print("Zle")
        else:
            print("Bardzo zle")
    else:
        if uzyskany_wynik >= 2120:
            print("Bardzo dobrze")
        elif uzyskany_wynik >= 1770:
            print("Dobrze")
        elif uzyskany_wynik >= 1400:
            print("Srednio")
        elif uzyskany_wynik >= 1050:
            print("Zle")
        else:
            print("Bardzo zle")