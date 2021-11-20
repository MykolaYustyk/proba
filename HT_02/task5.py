#
# 5. Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити). 
# 
# 
test_dict =  {'a': 12, 'b' : 15, 'c' : 12, 'd' : 15, 'e' : 1, 'f' : -2}
print("The original dictionary is : " , test_dict)
temp_dict = {val : key for key, val in test_dict.items()}
res_dict = {val : key for key, val in temp_dict.items()}
print("The dictionary after values removal : ", res_dict) 
