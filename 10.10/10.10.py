# in this exercise i try to count some words in 'some_text.txt'

with open('some_text.txt', encoding="utf-8", mode="r") as file:
    content = file.read().lower().split()

counter = 0

# try to find 'the' word in some_text.txt file
for word in content:
    if len(word) == 3 and word == "the":
        counter += 1

print(f"I found {counter} 'the' words.")
