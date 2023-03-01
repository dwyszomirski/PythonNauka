# Instrukcja in pozwala sprawdzic czy litera wystepuje w napisie
name = "Ala"
if "A" in name:
    print("W imieniu jest A!")
else:
    print("Nie ma A...")

# Mozemy za jej pomoca sprawdzic czy elementy wystepuja na liscie
ulubione_sporty = ["bieganie", "jazda na rowerze", "pływanie"]

if "koszykowka" in ulubione_sporty:
    print("Zagramy w kosza?")
else:
    print("hmmm...")

# Oraz czy klucze wystepuja w słowniku
person = {
    "first_name": "Dominik",
    "last_name": "Wyszomirski",
}
if "first_name" in person:
    print(person["first_name"])
if "car" in person:
    print(person["car"])
