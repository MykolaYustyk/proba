#
# 6. Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.
#
def funct (num) : 
    if num > 0 :
        result = num * num
    elif num < 0 :
        result = num + 100
    else:
        result = num
    return result

n = int(input("Input numeric value: "))
print("Result = ", funct(n))