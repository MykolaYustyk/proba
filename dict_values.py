input_dict = {1:'one', 2:'two', 3:'three', 4:'one', 5:'two', 6:'six'}
out_dict ={}
for key in input_dict:
    if input_dict[key] not in out_dict.values():
        out_dict[key] = input_dict[key]
print(out_dict)