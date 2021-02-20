while True:
    """This program sum two numbers. The program handles exceptions 'Value Error'"""
    try:
        first_number = int(input("Please input first number: "))
        second_number = int(input("Please input second number: "))
    except ValueError:
        print(f"You are entering non-digit number. Please enter a digit number.")
    else:
        print(f"The sum of your numbers is {first_number + second_number}")

