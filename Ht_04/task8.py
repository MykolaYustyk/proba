#
# 8. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. Тобто, функція приймає два аргументи: список і величину зсуву (якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
#  Наприклад:
#       fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
#       fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
#
def fnc(old_list, shift) :
    new_list = []
    if 0 < shift < len(old_list) - 1 :
        new_list = old_list[-shift:] + old_list[:len(old_list)-shift]
    elif shift < 0  :
        new_list = old_list[abs(shift):] + old_list[:abs(shift)]     
    return new_list  
list_of_values = input("Input list is: ").split(', ')
shift = int(input("shift = "))
print('Result = ', fnc(list_of_values, shift))