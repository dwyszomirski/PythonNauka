import speed_calculator
running_distance = float(input("Ile km przebiegles? "))
running_time = float(input("Ile godzin Ci to zajelo? "))

avg_speed = speed_calculator.avg_speed(running_distance, running_time)
print(f"Twoja srednia predkosc biegu to {avg_speed}km/h")