#
# 5. Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити). 
# 
# 
test_dict = {'a': 1, 'b': 3, 'c': 1, 'd': 5,'e': [1], 'f': "a", 'g': "a", 'h': [1]}
print("The original dictionary is : " , test_dict)

temp = []
result_dict = {}
for key, val in test_dict.items():
    if val not in temp:
        temp.append(val)
        result_dict[key] = val

print("The dictionary after values removal : " , result_dict)