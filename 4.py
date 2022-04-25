from random import randint


def random_number():
    # list with 100 numbers
    var = 0
    for i in range(1):
        var += randint(1, 100)
    return var


print(random_number())
