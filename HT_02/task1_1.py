#1. Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. Список можна "захардкодити".
#  Елементами списку повинні бути як рядки, так і числа.

input_list = [1, 23.5, 'one', -12, 'два']
print(input_list)
print(''.join(list(map(str, input_list))))