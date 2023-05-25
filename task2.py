# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

a = int(input("Insert a: "))
b = int(input("Insert b: "))


def ret_sum(a, b):
    if a > b:
        if b == 0:
            return a
        return ret_sum(a + 1, b - 1)
    else:
        if a == 0:
            return b
        return ret_sum(a - 1, b + 1)


print(ret_sum(a, b))