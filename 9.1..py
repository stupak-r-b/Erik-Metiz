class Restaurant():
    """Create restaurant object"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Output name of the restaurant"""
        print(f"The restaurant name is {self.restaurant_name} and we have {self.cuisine_type} kitchen.")

    def open_restaurant(self):
        """Output 'Open' if the store is open."""
        print(f"Our {self.restaurant_name} is open now!")


pizza_hut = Restaurant("Pizza Hut", "chinese")

pizza_hut.describe_restaurant()
pizza_hut.open_restaurant()