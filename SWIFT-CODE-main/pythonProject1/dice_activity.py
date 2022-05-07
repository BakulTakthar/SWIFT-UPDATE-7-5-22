import random


def dice_roll():
    total_outcomes = [1, 2, 3, 4, 5, 6]
    favourable1 = random.choice(total_outcomes)
    favorable2 = random.choice(total_outcomes)
    print(f"({favourable1}, {favorable2})")


# 3:47:52
