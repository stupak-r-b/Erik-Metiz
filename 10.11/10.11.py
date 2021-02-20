import json

def get_the_favorite_number():
    """This program takes users favorite number and save it in the json file"""
    favorite_number = input("Please enter your favorite number: ")
    file = "users_favorite_number.json"
    with open(file, 'w') as f:
        json.dump(favorite_number, f)

def users_favorite_number():
    """This program takes the number from json file and than greet the user."""
    with open("users_favorite_number.json", 'r') as f:
        users_favor_num = json.load(f)
        print(f"I know your favorite number. Your favorite number is {users_favor_num}")

get_the_favorite_number()
users_favorite_number()