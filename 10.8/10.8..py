#in this exercise i work with exception ==> FileNotFoundError

files = ['cats.txt', 'dogs.txt', 'elephants.txt']

for file in files:
    try:
        with open(file, 'r') as some_file:
            content = some_file.read()
    except FileNotFoundError:
        pass
    else:
        print(content)