# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input("How many numbers in massive? "))
x = int(input("Enter wishing number: "))
lst = []
counter = 1
while counter < n+1:
    lst.append(counter)
    counter+=1

etalon=0
for num in range(len(lst)):
    if (x-lst[num])<x-etalon and x-lst[num]>0:
        etalon=num
print(lst[etalon])


