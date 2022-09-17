#число
a = 60
b = 12
if a % b == 0:
    print(a//b)

#слово
my_mame = "Marina"
my_surname = "Polishova"
print(my_surname, my_mame)

#строки
a = "HEOEVEIEIE EGEOEDE!E"
a = a.split("E")
print(a)

#список
chet = []
nechet = []
for i in range(1,67):
    if i % 2 == 0:
        chet.append(i)
    else:
        nechet.append(i)
print("Нечетные цифры:", nechet)
print("четные цифры:", chet)

#кортеж
k = "Hello World"
print(tuple(k))