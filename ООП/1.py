class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_car(self):
        print(self.brand, self.model, self.year)


class ElectricCar(Car):
    def __init__(self, battery_size, change_level, brand, model, year):
        super().__init__(brand, model, year)
        self.battery_size = battery_size
        self.change_level = change_level

