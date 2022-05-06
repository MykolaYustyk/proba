#
#
# 1. Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.
#
#
import math
def square(side) :
    result = (4*side, side**2, side * math.sqrt(side))
    return result

side = float(input('Input length of square: '))
print('Results = ', square(side))