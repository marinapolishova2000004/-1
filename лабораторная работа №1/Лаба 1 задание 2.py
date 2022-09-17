from math import *
f = input("Введите необходимую функцию (сложение, вычитание, умножение, деление, возведение в степень, логарифм, "
          "\n округление в большую сторону до N знака после запятой, округление в меньшую сторону до N знака после запятой): ")

a = input("Введите первый элемент:")
if a in "йцукенгшщзхъфывапролджэячсмитьбю" or a in "qwertyuiopasdfghjklzxcvbnm":
    print("Введенный элемент не является числом, введите первый элемент:")
    a = int(input())
else:
    a = float(a)

b = input("Введите второй элемент:")
if b in "йцукенгшщзхъфывапролджэячсмитьбю" or b in "qwertyuiopasdfghjklzxcvbnm":
    print("Введенный элемент не является числом, введите второй элемент:")
    b = int(input())
else:
    b = float(b)

if f == "сложение":
    print(a + b)
elif f == "вычитание":
    print(a - b)
elif f == "умножение":
    print(a * b)
elif f == "деление":
    if b == 0:
        print("Ошибка")
    else:
        print(a / b)
elif f == "возведение в степень":
    print(a ** b)
elif f == "логарифм":
    print(log(a,b))
elif f == "округление в большую сторону до N знака после запятой":
    if b == 0:
        print(ceil(a))
    else:
        papa = modf(a)
        print(papa[1] + ceil(papa[0] * (10 ** b)) / ((10 ** b)))
elif f == "округление в меньшую сторону до N знака после запятой":
    if b == 0:
        print(floor(a))
    else:
        papa = modf(a)
        print(papa[1] + floor(papa[0] * (10 ** b)) / ((10 ** b)))