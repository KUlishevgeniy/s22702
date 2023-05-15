def create_car(color, consumption, tank_volume, mileage=0):
return {
"color": color,
"consumption": consumption,
"tank_volume": tank_volume,
"reserve": tank_volume,
"mileage": mileage,
"engine_on": False
}
def start_engine(car):
if not car["engine_on"] and car["reserve"] > 0:
car["engine_on"] = True
return "Двигатель запущен."
return "Двигатель уже был запущен."
def stop_engine(car):
if car["engine_on"]:
car["engine_on"] = False
return "Двигатель остановлен."
return "Двигатель уже был остановлен."


def drive(car, distance):
if not car["engine_on"]:
return "Двигатель не запущен."
if car["reserve"] / car["consumption"] * 100 < distance:
return "Малый запас топлива."
car["mileage"] += distance
car["reserve"] -= distance / 100 * car["consumption"]
return f"Проехали {distance} км. Остаток топлива: {car['reserve']} л."


def refuel(car):
car["reserve"] = car["tank_volume"]


def get_mileage(car):
return f"Пробег {car['mileage']} км."


def get_reserve(car):
return f"Запас топлива {car['reserve']} л."


car_1 = create_car(color="black", consumption=10, tank_volume=55)

print(start_engine(car_1))
print(drive(car_1, 100))
print(drive(car_1, 100))
print(drive(car_1, 100))
print(drive(car_1, 300))
print(get_mileage(car_1))
print(get_reserve(car_1))
print(stop_engine(car_1))
print(drive(car_1, 100))
