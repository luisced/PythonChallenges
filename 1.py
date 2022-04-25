def capital_indexes(word):
    li = []
    for i in word:
        if i.isupper():
            li.append(word.index(i))

    return li


print(capital_indexes("HeLoO"))
