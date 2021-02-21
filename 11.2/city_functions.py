def where_do_you_live(country, city, population=1_000_000):
    """this function returns a formatted string"""
    place = f"{country.title()}, {city.title()} - population {population}"
    return place
