import unittest
from employee import Employee


class EmployeeFunctionCase(unittest.TestCase):
    def setUp(self):
        self.some_employee = Employee("Bob", "Dylan", 10_000_000)

    def test_give_default_rise(self):
        self.some_employee.give_raise()
        self.assertEqual(self.some_employee.year_salary, 10_005_000)

    def test_give_custom_raise(self):
        self.some_employee.give_raise(10_000)
        self.assertEqual(self.some_employee.year_salary, 10_010_000)