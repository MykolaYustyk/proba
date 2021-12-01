#7. Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж) і повертає генератор, який буде вертати значення з цієї послідовності, при цьому, якщо було повернено останній елемент із послідовності - ітерація починається знову.
#  Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
#   >>>for elem in generator([1, 2, 3]):
#   ...    print(elem)
#   ...
#   1
#   2
#   3
#   1
#   2
#   3
#   1
#   .......
#
def generator(input_list) :
    for i in input_list : 
        yield i 
        
def gen(input_list) :
    while True:
        for elem in generator(input_list) :
            print(elem)
          
         
input_list = [1, 3, 4]
gen(input_list)
