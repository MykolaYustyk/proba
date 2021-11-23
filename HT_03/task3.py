#
#
#3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)
#
#
def season(month) : 
    if month in [1, 2, 12] : 
        print("Winter")
    elif month in [3, 4, 5] : 
        print('Spring')
    elif month in [6, 7, 8] : 
        print("Summer")
    else : 
       print('Autumn')
    
    return

mon = int(input("Input nomber of month : ")) 
season(mon) 

     