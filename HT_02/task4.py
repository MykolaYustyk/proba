#
# 4. Написати скрипт, який об'єднає три словника в новий. Початкові словники не повинні змінитись. Дані можна "захардкодити".
#       Sample Dictionary :
#        dict_1 = {1:10, 2:20}
#        dict_2 = {3:30, 4:40}
#        dict_3 = {5:50, 6:60}
#        Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#
dict_1 = {1:10, 2:20}
dict_2 = {3:30, 4:40}
dict_3 = {5:50, 6:60}
result_dict ={}
result_dict = dict_1.copy()
result_dict.update(dict_2)
result_dict.update(dict_3)
print('dict_1: \n', dict_1)
print('dict_2: \n', dict_2)
print('dict_3: \n', dict_3)
print('Result is : \n', result_dict)
