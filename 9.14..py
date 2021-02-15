from random import randint
"""It's a lottery game."""

some_data = [3, 4, 6, 34, 65, 9, 76, 58, 87, 23, "d", "g", "e", "к", "c"]

print("Выигрышный билет содержит комбинацию:")
for i in range(4):
    """
    С помошью метода randint выберем случайный индекс для списка some_data.
    (Используя метод len, подсчитаем длину списка и используем данное значение для
    вывода случайного символа из списка используя метод randint())
    """
    random_data = randint(0, len(some_data)-1)
    print(some_data[random_data], end="")


