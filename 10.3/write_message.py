filename = "guest.txt"

guest_name = input("Input your name please: ")

with open(filename, "w") as file:
    file.write(guest_name)

