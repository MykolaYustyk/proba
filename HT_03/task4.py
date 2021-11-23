# 4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат. 
# Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат. 
# Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3
#
def func1(val) : 
    result = val* val
    return result

def func2(val) : 
    result = val ** 3
    return result

def func3(val) : 
    result = val/ 4
    return result

def funct4(val) : 
    result = func1(val) + func2(val) + func3(val)
    return result

x = int(input("Введіть ціле х: "))
print('f(', x, ") =", funct4(x))
