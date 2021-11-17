"""
1 .Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
        Sample data : 1, 5, 7, 23
        Output :
        List : [‘1', ' 5', ' 7', ' 23']
        Tuple : (‘1', ' 5', ' 7', ' 23')
"""

print('Write a some of comma-separated numbers ')
lst = input().split(',')
print('list: ', lst)
print('tuple:', tuple(lst))