# 6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#  P.S. Повинен вертатись генератор.
#  P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
#
class StepError(Exception) :
    pass

def range_gen(stop, start=0, step=1) :
    if step > 0 :
        i = start
        while i < stop :
            yield i
            i += step
    elif step < 0:
        i = start
        while i > stop :
            yield i
            i += step
    else: 
         raise StepError("Step must be non equal zero")              

start = int(input('Start value is: '))
stop = int(input("stop value is: "))
step = int(input('step = '))

try:
    for elem in range_gen( stop, start, step) : 
        print(elem, end = ' ')
except StepError as err :
    print(err)
finally :
    print('\n')
    rez = list(range_gen( stop, start, step))
    print(rez)
    print(" Stop")