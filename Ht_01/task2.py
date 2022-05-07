#2.Write a script to print out a set containing all the colours from color_list_1 which are not present in color_list_2.
#      Test Data :
#      color_list_1 = set(["White", "Black", "Red"]) 
#      color_list_2 = set(["Red", "Green"])
#      Expected Output :
#      {'Black', 'White'}

color_list_1 = set(input("Input first colors list: ").split(", "))
color_list_2 = set(input("Input second colors list: ").split(", "))
out_list = set(color for color in color_list_1 if color not in color_list_2)
print('Output set is : \n', out_list)