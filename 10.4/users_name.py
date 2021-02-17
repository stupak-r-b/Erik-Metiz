file_name = "guest_book.txt"
while True:
    guest_name = input("Input your name please: ")
    print(f"Hello, {guest_name}!")
    with open(file_name, "a") as file:
        file.write(guest_name + "\n")