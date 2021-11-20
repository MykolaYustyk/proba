#1. Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. Список можна "захардкодити".
#  Елементами списку повинні бути як рядки, так і числа.

input_list = [1, 23.5, 'one', -12, 'два']
out_string = ''
print(input_list)
for value in input_list :
    out_string += str(value)
print(out_string)
