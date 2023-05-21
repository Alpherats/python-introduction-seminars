# даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. затем пользователь вводит сами элементы множеств.

def fill_lst(amont_of_elem):
    counter = 0
    lst = []
    while counter<amont_of_elem:
        elem = int(input("insert number: "))
        lst.append(elem)
        counter += 1
    return lst

def clear_lst(some_slt):
    sorted_lst = []
    for elem in some_slt:
        if elem not in sorted_lst:
            sorted_lst.append(elem)
    return sorted_lst


n = int(input("insert n: "))
m = int(input("insert m: "))

lst_n = fill_lst(n)
lst_m = fill_lst(m)

new_lst = clear_lst(lst_n+lst_m)
print(sorted(new_lst))
