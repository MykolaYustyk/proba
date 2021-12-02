'''
1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Green
      Yellow     Green
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
      .......
'''
import time
auto_light = [['Red', 'Yellow'], ['Green', "Yellow"]]
footer_light = ['Green', 'Red']
i = 0
while True :
    
    j=0
    while j < 6 :
        if j < 4:
            print((auto_light[i][0]).ljust(8), ' ', footer_light[i].ljust(8))
        else:
            print((auto_light[i][1]).ljust(8), ' ', footer_light[i].ljust(8)) 
        time.sleep(1)    
        j += 1    
    i += 1
    if i == 2 :
       i = 0
    