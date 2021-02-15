from random import randint

class Die:
    """The class show us nums from 1 to 6 including 6 using roll_die method."""

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        return randint(1, self.sides+1)


"""Go play with it."""
some_game = Die()
print(some_game.roll_die())