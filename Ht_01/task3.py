"""

3. Write a script to sum of the first n positive integers.

"""
n = int(input("Write number of the first positive integers \n"))
s = sum(num for num in range(1, n + 1))
print('s =', s)
