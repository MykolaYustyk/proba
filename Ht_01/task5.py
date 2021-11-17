# 5. Write a script to convert decimal to hexadecimal
#       Sample decimal number: 30, 4
#       Expected output: 1e, 04

numbers = input('Input some decimal numbers : \n').split(', ')
print('Output numbers :\n')
for i in range((len(numbers))):
      numbers[i]=hex(int(numbers[i]))[2:]
      if i < len(numbers)-1 :
            print(numbers[i]+', ', end='')
      else :
            print(numbers[i])