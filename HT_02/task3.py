#
#    3. Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".
#   Sample data: [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
#    Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
#
input_list = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
print(input_list)
output_list =[element for element in input_list if  element]
print(output_list)
