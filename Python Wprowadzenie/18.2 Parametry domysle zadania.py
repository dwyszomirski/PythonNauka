# Funkcja zakresu +/- 10
# def value_with_tolerance(value, tolerance_percentage=10):
#     tolerance_value = tolerance_percentage * value / 100
#     return [value - tolerance_value, value + tolerance_value]
#
# print(value_with_tolerance(value=100))
# print(value_with_tolerance(value=100, tolerance_percentage=40))

# Zadanie 2
def add_people_to_calsses(name_str, participants=None):
    if participants is None:
        participants = []
    names = name_str.split(',')
    for name in names:
        participants.append(name)
    return participants

attendees_names = "Ola,Bob,Ala,Kuba"
monday_coures_participants = add_people_to_calsses(attendees_names)
print(monday_coures_participants)
attendees_names = "Pawel,Dominika"
monday_coures_participants = add_people_to_calsses(attendees_names, participants=monday_coures_participants)
print(monday_coures_participants) 

attendees_names = "Ania,Krzysztof"
friday_coures_participants = add_people_to_calsses(attendees_names)
print(friday_coures_participants)