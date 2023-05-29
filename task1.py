# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def calc_progression(n, a1, d):
    progression = [a1]
    for i in range(2, n + 1):
        an = a1 + (i - 1) * d
        progression.append(an)
    print(progression)


calc_progression(int(input("Insert amount of elements: ")), int(input("Insert a1: ")), int(input("Insert d: ")))
