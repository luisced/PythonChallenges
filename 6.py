def double_letters(word):
    li = []
    for i in word:
        if word.count(i) > 1:
            li.append(i)
    return li


print(double_letters("Hello"))
