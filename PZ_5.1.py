# Описать функцию Power1(A, B) вещественного типа, находящую величину AB по
# формуле AB = exp(B*ln(A)) (параметры A и B — вещественные). В случае нулевого
# или отрицательного параметра A функция возвращает 0. С помощью этой функции
# найти степени AP , BP , CP , если даны числа P, A, B, C. #

import math


def grisha(a, b):
    if a <= 0:
        return 0
    else:
        return math.exp(b * math.log(a))


P = 2
A = 3
B = 4
C = 5
AP = grisha(A, P)
BP = grisha(B, P)
CP = grisha(C, P)

print("Вывод AB", AP)
print("Вывод BP", BP)
print("Вывод CP", CP)
