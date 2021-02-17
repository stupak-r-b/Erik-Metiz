filename = "learning_python.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

for i in range(3):
    for line in lines:
        print((line.replace("Python", "JavaScript").rstrip()))
    print()