list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
maxim = 0
for i in list_numbers:
    if i > maxim:
        maxim = i
x = list_numbers.index(maxim)
list_numbers[x], list_numbers[-1] = list_numbers[-1], list_numbers[x]

# TODO Оформить решение

print(list_numbers)
