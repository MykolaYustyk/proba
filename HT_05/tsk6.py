# 6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#  P.S. Повинен вертатись генератор.
#  P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
#
class StepError(Exception) :
    pass

def range_gen(start=0, stop='', step='') :
    if stop == '':
        stop = start
        start = 0
    if step == '':
        step = 1
    else:
        step = int(step)            
    if step > 0 :
        i = start
        while i < int(stop) :
            yield i
            i += step
    elif step < 0:
        i = start
        while i > int(stop) :
            yield i
            i += step
    else: 
         raise StepError("Step must be non equal zero")              
stop = ''
step = ''
start = int(input('Start value is: '))
stop = input("stop value is: ")
step = input('step = ')
try:
    for elem in range_gen(start, stop, step) : 
        print(elem, end = ' ')
except StepError as err :
    print(err)
finally :
    print('\n')
    rez = list(range_gen(start, stop, step))
    print(rez)
    print(" Stop")