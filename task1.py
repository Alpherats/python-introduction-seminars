# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import random

n = int(input("How many numbers? "))
need_num = int(input("What number are we searching for? "))
lst = []
x=0
counter = 0

while counter < n:
    rand_num = random.randint(0,20)
    lst.append(rand_num)
    counter+=1
print(f"before {lst}")

for num in range(len(lst)):
    if need_num is lst[num]:
        x +=1
lst.append(x)
print(f"after {lst}")