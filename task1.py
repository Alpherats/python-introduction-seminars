#Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

a = int(input("Insert a: "))
b = int(input("Insert b: "))

def recur(a,b):
    if b ==1:
        return a
    return a*recur(a, b-1)
print(recur(a,b))