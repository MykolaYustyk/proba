"""
7. Написати скрипт, який отримає максимальне і мінімальне значення із словника. Дані захардкодити.
                Приклад словника (можете використовувати свій):
                dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
                Вихідний результат:
                MIN: 10
                MAX: 60
"""
dict_1 = {1: -10, 2: 20, 3: 30, 4: 40, 5: 50, 6: -60}
print(dict_1);
values_of_dict = dict_1.values()
max_value = max(values_of_dict)
min_value = min(values_of_dict)
print("Output results\n", 'MAX: ', max_value, "\n", 'MIN : ', min_value)
