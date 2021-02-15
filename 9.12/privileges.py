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