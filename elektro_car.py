class Car():
    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odomrter(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print(f"This car has a {self.battery_size} - kWt battery.")

class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя"""
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2016)
