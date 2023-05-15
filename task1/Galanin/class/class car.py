import time
class car():
    def __init__(self, colour, brand,gas):
        self.colour= colour
        self.brand= brand
        self.gas = gas
        self.gasn = gas
        self.spending = 5
        self.delta = 0
    def driving(self):
        self.time1 = time.time()
    def stop(self):
        self.time2 = time.time()
        self.delta = self.time2 - self.time1

        self.fuel = round(int(self.gas) - (self.delta * self.spending))
        self.gas=self.fuel
        if self.fuel > 0:
            print(f"""марка: {self.brand}
цвет: {self.colour}
объем бака: {self.gasn}
остаток топлива: {self.fuel}""")
        else:
            print('Нет топлива')
auto = car('white', 'lada', 500)
auto.driving()
time.sleep(5)
auto.stop()
auto.driving()
time.sleep(5)
auto.stop()