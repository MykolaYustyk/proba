# 6. Write a script to check whether a specified value is contained in a group of values.
#         Test Data :
#         3 -> [1, 5, 8, 3] : True
#         -1 -> (1, 5, 8, 3) : False
val = input('Input value for search : \n')
search_list = input('Input list: \n').split(', ')
val_in_list = False
if val.strip() in search_list :
    val_in_list = True
print(val," -> ", search_list, ": ", val_in_list)
