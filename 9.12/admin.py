from user import User
from privileges import Privileges


class Admin(User):
    """This class inherits the attributes from class User"""

    def __init__(self, first_name, last_name, age, phone_number):
        super().__init__(first_name, last_name, age, phone_number)
        self.admin_privileges = Privileges()