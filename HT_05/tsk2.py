#2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
#   - щось своє :)
#   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
#
class NameValidationException(Exception):
    pass

class PassValidationException(Exception) :
    pass

def user_validation (name, password) :
    result = False
    if not (3 <= len(name) <= 50) :
        raise NameValidationException("ім'я повинно бути не меншим за 3 символа і не більшим за 50")
    if not (len(password) >= 8 and password.isalnum() and not password.isdigit() and not password.isalpha()):
        raise PassValidationException("пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру")
    else:
        result = True
    return result    

name = input('Input your name : ')
password = input('Your password : ')
rez = False
try:
    rez = user_validation(name, password)
    print(" Result is : ", rez)
except (NameValidationException, PassValidationException) as exc :
    print(exc)
finally:
    print("Stop")
   

