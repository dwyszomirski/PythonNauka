def average_speed(distance, time):
    return distance / time

def run_avg_speed_calculator(vehicle_name):
    distance = float(input(f"Ile km pokonales za pomoc {vehicle_name}? "))
    time = float(input("Ile godzin Ci to zajelo? "))
    avg_speed = average_speed(distance=distance, time=time)
    print(f"Twoja srednia predkosc przemieszczania sie za pomoca {vehicle_name} to {avg_speed}km/h")

run_avg_speed_calculator(vehicle_name="biegu")
run_avg_speed_calculator(vehicle_name="roweru")
run_avg_speed_calculator(vehicle_name="samochodu")