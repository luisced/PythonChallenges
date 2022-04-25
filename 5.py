def only_ints(n1, n2):
    if isinstance(n1, int) and isinstance(n2, int):
        return True
    else:
        return False


print(only_ints("a", "6"))


def only_intss(n1, n2):
    if type(n1) == int and type(n2) == int:
        return True
    else:
        return False


print(only_intss(2, 1))
