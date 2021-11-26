#
#
# 1. Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.
#
#
def square(side) :
    result = (4*side, side**2, side * 1.41)
    return result

side = float(input('Input length of square: '))
print('Results = ', square(side))