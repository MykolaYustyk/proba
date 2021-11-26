#
#
# 4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.
#
#
def is_prime(digit) :
    result = True
    for i in range(2, digit-1):
        if digit % i == 0:
            result = False
            break  
    return result

def prime_list(start_val, end_val) :
    result = []
    for digit in range(start_val, end_val + 1) :
        if is_prime(digit) :
            result.append(digit)
    return result

start_value = int(input('Start value :'))
end_value = int(input('End value: '))
print('Result = \n', prime_list(start_value, end_value))
