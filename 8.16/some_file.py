def make_car(manufacturer: str, model: str, **kwargs):
    color = list(kwargs.keys())[0]
    model = list(kwargs.values())[0]
    return color, model


car = make_car('subaru', 'outback', color="blue", tow_package=True)
print(car)
