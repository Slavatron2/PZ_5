# Составить функцию, которая выполнит суммирования числового ряда #

a = input("Введите количество чисел -")
b = input("Введите числа -")
amogus = 0
try:
    a = int(a)
    b = int(b)
except ValueError:
    print("Ошибка")
for i in range(a):
    amogus += b
print(amogus)
