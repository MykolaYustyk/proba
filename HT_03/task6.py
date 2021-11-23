# 6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
#    Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
# -  якщо довжина бульше 50 - > ваша фантазiя
#
def string_work_50(str) : 
    count_of_digit = 0
    count_of_letters = 0
    for leter in range(len(str)) :
        if str[leter].isalpha() :
            count_of_letters += 1
        if str[leter].isdigit() :
            count_of_digit += 1
    print("Length of sting = ", len(str), ". Count of letters =", count_of_letters,". Count of digits =", count_of_digit)
    return

def string_work_30(str) :
    new_string =''
    sum = 0 
    
    for leter in range(len(str)) :
        if str[leter].isalpha() :
            new_string += str[leter]
        if str[leter].isdigit() :
            sum += int(str[leter])
        
    print("String without digits: ", new_string)
    print("Сума цифр :", sum)
    return
 
def string_work(str) : 
    if 30 < len(str) < 50 :
        string_work_50(str)
    elif len(str) < 30 :
        string_work_30(str)
    else:
        print("Наша фантазія")
    return
    
str = input("Input string \n")
print("Results of program \n")
print
string_work(str)