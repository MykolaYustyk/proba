#
# 3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це число просте, и False - якщо ні.
#
def is_prime(digit) :
    result = True
    for i in range(2, digit+1):
        if digit % i == 0:
            result = False
            break  
    return result
n = int(input("Input integer from 0 to 1000 "))
print('Result =', is_prime(n))