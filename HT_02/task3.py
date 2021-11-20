#
#    3. Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".
#   Sample data: [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
#    Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
#
input_list = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
output_list = []
print(input_list)
for current_element in range(len(input_list) - 1):
    if len(input_list[current_element]) != 0:
        output_list.append(input_list[current_element])
print(output_list)
