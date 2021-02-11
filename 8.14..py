def make_car(manufacturer: str, model: str, **kwargs):
    return kwargs


car = make_car('subaru', 'outback', color="blue", tow_package=True)
print(car)
