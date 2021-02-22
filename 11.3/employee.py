class Employee:
    """This class create an object that save users name, surname and year salary."""

    def __init__(self, name, surname, year_salary):
        self.name = name
        self.surname = surname
        self.year_salary = year_salary

    def give_raise(self, rise=5000):
        """This method increases year salary on 5000$"""
        self.year_salary += rise