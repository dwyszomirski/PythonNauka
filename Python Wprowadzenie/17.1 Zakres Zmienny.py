# Zmienna zdefiniowana wewnatrz funkcji
# def failes_modify_global_name():
#     name = "Kuba"
#     print(f"Wewnatrz funkcji: {name}")
# name = "Mikołaj"
# print(f"Przed funkcja: {name}")
# failes_modify_global_name()
# print(f"Po funkcji: {name}")

# def succes_modify_global_name():
#     global name
#     name = "Kuba"
#     print(f"Wewnatrz funkcji: {name}")
# name = "Mikołaj"
# print(f"Przed funkcja: {name}")
# succes_modify_global_name()
# print(f"Po funkcji: {name}")

PI_NUMBER = 3.141
def circle_area(radius):
    return PI_NUMBER * radius * radius
print(circle_area(radius=30))