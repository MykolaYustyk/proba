"""
2. Написати скрипт, який пройдеться по списку, який складається із кортежів, і замінить для кожного кортежа останнє значення.
   Список із кортежів можна захардкодити. Значення, на яке замінюється останній елемент кортежа вводиться користувачем.
   Значення, введене користувачем, можна ніяк не конвертувати (залишити рядком). Кількість елементів в кортежу повинна бути різна.
             Приклад списка котежів: [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,)]
             Очікуваний результат, якщо введено "100":
        Expected Output: [(10, 20, "100"), (40, 50, 60, "100"), (80, "100"), ("100",)]
        
"""
input_list =[(20, 30, 40), (70, 60, 500, 800), (-10, 20), (1, 2, 3, 4, 5), (15000,)]
out_list =[]
change_value = input('Input value wich you want change each last element: ')
for current_tuple in input_list :
    current_tuple = list(current_tuple)
    current_tuple[-1] = change_value
    current_tuple = tuple(current_tuple)
    out_list.append(current_tuple)
print('Output list is : \n', out_list)
