#
# 7. калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
#
def calculation(first_digit, operation, second_digit) :
    if operation == '+' :
        result = float(first_digit) + float(second_digit)
    elif operation == '-' : 
        result = float(first_digit) - float(second_digit)
    elif operation == "/" and second_digit != 0 :
        result = float(first_digit) / float(second_digit)
    elif operation == "*" :
        result = float(first_digit) * float(second_digit)
    else :
        result = 0       
    return result
    
print("Введіть числа і операцію розділені пробілами. \n Наприклад: 2 + 5. \n", end='')
instruction = input().split()
res = calculation(instruction[0], instruction[1], instruction[2])
print("=", "{:.2f}".format(res))

