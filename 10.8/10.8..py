#in this exercise i work with exception ==> FileNotFoundError

files = ['elephants.txt', 'cats.txt', 'dogs.txt']

for file in files:
    try:
        with open(file, 'r') as some_file:
            content = some_file.read()
    except FileNotFoundError:
        print(f"The file {file} is not found.")
    else:
        print(content)