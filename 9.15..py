from random import randint


#try to selection of the winning combination
wining_combination = "34g4c"
some_data = [3, 4, 6, 34, 65, 9, 76, 58, 87, 23, "d", "g", "e", "k", "c"]
counter = 0

while True:
    combination = ""
    for i in range(4):
        random_combination = randint(0, len(some_data)-1)
        combination += str(some_data[random_combination])
    if combination == wining_combination:
        print(f"Congratulations.You win after {counter} tries.")
        break
    else:
        counter += 1