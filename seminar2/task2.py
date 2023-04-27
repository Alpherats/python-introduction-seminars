# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
import math

s = int(input("insert s: "))
p = int(input("insert p : "))

disc = s*s-4*p

x11 = (s+math.sqrt(disc))/2
x12 = (s-math.sqrt(disc))/2
print(x11)
print(x12)
if x11>0 and x12<=1000:
  y21 = p/x12
  print(f"x - {x12}, y - {y21}")
elif x12> 0 and x11<=1000:
  y22 = p/x11
  print(f"x - {x11}, y - {y22}")
else:
  print("Числа задуманы неверные")