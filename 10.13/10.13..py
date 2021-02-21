import json

def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username(another_user=""):
    """
    Запрашивает новое имя пользователя.
    Если another_user заполнен, то в систему вошел
    не предыдущий пользователь и необходимо обновить данные.
    """
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(another_user, f)
    return another_user



def greet_user():
    """Приветствует пользователя по имени."""
    name = input("Hello! What's your name?: ")
    username = get_stored_username()

    # Проверяем, что вошедший пользователь это пользователь из предыдущей сессии
    if username == name:
        print(f"Welcome back, {username}!")

    # создаем нового пользователя и указываем его имя
    else:
        username = get_new_username(another_user=name)
        print(f"We'll remember you when you come back, {username}!")

greet_user()