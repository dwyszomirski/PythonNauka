#   Typy Immutable:          Typy Mutable:
#   Int                      List
#   Float                    Dict
#   Str                      Set
#   Bool                     Klasy własne
#   NoneType
#   tuple, forozenset
#   frozen dataclass

# Hash zwraca dla tego samego obkietu zawsze jest taki sam
# Obkiet mozna porownac z innymi(ma wlasna lub domyslana metode _eq_)
# Hashable - podsumowanie
# 1. Hashowalne obkiekty moga byc kluczami w słowniku
# 2. Typy proste immutable(int, str) sa hashowalne
# 3. Kontenery mutable(list, dict) nie sa hashowalne
# 4. Kontenery immutable sa hashowalne jezeli ich elementy sa immutable
# 5. KLasy wlasne sa domyslne Hashowalne
# 6. Majac wlasne _eq_ w klasie mutalbe nie mozna implementowac _hash_
# 7. Jezeli klasa ma wlasne _eq_ a nie ma _hasha_ to nie jest hashowalna


# list-mutable
shooping_list = ["chleb"]
my_list = shooping_list
shooping_list.append("ser")

# str-immutable
name = "Mikołaj"
my_name = name
name = "Kuba"
print(my_name) # Mikołaj


def fun_with_default_immutable(number=2):
    number += 1
    print(number)


def func_with_default_mutable(numbers=[]):
    numbers.append(1)
    print(numbers)


func_with_default_mutable()
func_with_default_mutable()
func_with_default_mutable()

fun_with_default_immutable()
fun_with_default_immutable()
fun_with_default_immutable()