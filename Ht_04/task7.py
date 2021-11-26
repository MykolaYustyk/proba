#
# 7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.
#
def count_of_same(values_list):
    set_of_values = set(values_list)
    for value in set_of_values :
        print(value, "зустрічається ", values_list.count(value), "раз")
    return

values_list=input("Input list: \n").split(', ')
count_of_same(values_list)