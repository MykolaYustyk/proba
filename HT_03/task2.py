#
# 2. Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).
#
first_year = int(input('Введіть перший рік '))
end_year = int(input('Введіть останній рік '))
print()
print('Високосні роки на цьому проміжку такі: ')
for year in range (first_year, end_year+1) : 
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 : 
        print(year, end=", ")
        