"""

4. Write a script to concatenate N strings.

"""

n = int(input("Input number of strings \n"))
str = ''
for i in range(n) :
    str += input()
print('Output string = ',str)