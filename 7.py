def add_dots(word):
    # add dots between every letter
    for i in range(len(word)):
        word = word[:i] + "." + word[i:]
    return word


print(add_dots("Hello"))
