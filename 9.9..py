class Car:
    """Простая модель автомобиля."""

    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year}, {self.manufacturer}, {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size=75):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size
        self.rang_e = None

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            self.rang_e = 260
        elif self.battery_size == 100:
            self.rang_e = 315
        print(f"This car can go about {self.rang_e} miles on a full charge.")

    def upgrade_battery(self):
        """This method upgrade battery power up to 100 kWt."""
        if self.battery_size == 100:
            print(f"Your battery size already upgraded and it's power 100 kWt.")
        else:
            self.battery_size = 100
            print(f"Congratulations we upgrade your battery power up to 100 kWt.")

class ElectricCar(Car):
    """
    Представляет аспекты машины, специфические для электромобилей.
    Затем инициализирует атрибуты, специфические для электромобиля.
    """

    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


my_new_tesla = ElectricCar("Tesla", "Tesla Model X", 2021)
my_new_tesla.battery.describe_battery()
my_new_tesla.battery.upgrade_battery()
my_new_tesla.battery.describe_battery()