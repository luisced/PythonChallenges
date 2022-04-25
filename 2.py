from ast import Num
from os import WCOREDUMP


def mid(word):
    var = len(word)
    if var % 2 == 0:
        return word[var // 2 - 1:var // 2 + 1]
    else:
        return word[var // 2]
