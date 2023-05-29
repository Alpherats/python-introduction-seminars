# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random


def generate_arr(num_of_el):
    lst = []
    for num in range(num_of_el):
        lst.append(random.randint(0, 20))
    print(lst)
    return lst


def find_indexes(lst):
    for num in range(len(lst)):
        if min_val <= lst[num] <= max_val:
            print(f"Index of element in range - {num}, it's value - {lst[num]}")


new_lst = generate_arr(int(input("Amount of elements: ")))
min_val = int(input("Insert min value: "))
max_val = int(input("Insert max value: "))
find_indexes(new_lst)
