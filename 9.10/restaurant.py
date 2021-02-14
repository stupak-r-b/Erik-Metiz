class Restaurant:
    """Creates a restaurant object with a description
    and show us the number of visitors served."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Output name of the restaurant"""
        print(f"The restaurant name is '{self.restaurant_name.capitalize()}' and we have {self.cuisine_type} kitchen.")

    def open_restaurant(self):
        """Output 'Open' if the store is open."""
        print(f"Our {self.restaurant_name} is open now!")

    def set_number_served(self, number_of_visitors):
        """Sets the number of visitors who have visited the restaurant today."""
        if number_of_visitors >= 0:
            self.number_served = number_of_visitors
        print(f"Today we served {self.number_served} visitors.")

    def increment_number_served(self, number_of_visitors):
        """Increases the number of visitors who have visited the restaurant today."""
        if number_of_visitors >= 0:
            self.number_served += number_of_visitors
        print(f"Today we served {self.number_served} visitors.")