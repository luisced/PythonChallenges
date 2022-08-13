import enum


list1 = [0, 1, 2, 10, 4, 5, 6, 7, 8, 9]
max_number = list1[0]
for i in list1:
    if i > max_number:
        max_number = i

print(max_number)


x = (50 *(50 + 1))/2


n = 0
for i in range(51):
    n += i
print(f"El resultado es: {n}")