"""User class. This class takes data from user.
    This class also can show us the number of login attempts"""
class User:
    def __init__(self, first_name, last_name, age, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.login_attempts = 0

    """Output user phone number"""
    def describe_user(self):
        print(f"Информация о пользователе: "
              f"\n1.First name - {self.first_name};"
              f"\n2.Last name - {self.last_name};"
              f"\n3.Age - {self.age};"
              f"\n4.Phone number - {self.phone_number}.\n")

    def greet_user(self):
        print(f"\nДобро пожаловать на наш сервис {self.first_name.title()} {self.last_name.title()}!\n")

    def increment_login_attempts(self):
        """Increases the value of variable by 1."""
        self.login_attempts += 1
        print("Количество входов пользователя увеличено на 1. "
              f"Общее кол-во входов пользователя {self.first_name.title()} {self.last_name.title()} составляет {self.login_attempts}.")

class Privileges:
    """This class show us admin privileges."""

    def __init__(self):
        self.privileges = ["разрешено добавлять сообщения",
                           "разрешено удалять пользователей",
                           "разрешено банить пользователей"]

    def show_privileges(self):
        print("Administrator privileges list: ")
        for privilege in self.privileges:
            print(f"\t-{privilege.capitalize()};")

class Admin(User):
    """This class inherits the attributes from class User"""

    def __init__(self, first_name, last_name, age, phone_number):
        super().__init__(first_name, last_name, age, phone_number)
        self.admin_privileges = Privileges()


new_user = Admin("Roman", "Stupak", 27, "+48578489897")
new_user.admin_privileges.show_privileges()
