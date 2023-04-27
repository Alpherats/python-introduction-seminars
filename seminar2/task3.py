#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите N: "))
counter = 0
if n>0:
    while counter<n+1:
        print(f"Степень двойки 2*{counter} = {2**counter}")
        counter+=1
else:
    print("Введите положительное число")