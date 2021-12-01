# 1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
#  Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
#  Логіка наступна:
#       якщо введено коректну пару ім'я/пароль - вертається <True>;
#       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException
class LoginException(Exception) :
    pass

def check_login(username, password, silent = False) :
    current_user = list()
    result = False
    users_list = [['user1', "password1"],
                  ['user2', 'password2'],
                  ["user3", 'password3'],
                  ['user4', 'password4'],
                  ['user5', 'password5']]
    current_user.append(username)
    current_user.append(password)
    if current_user in users_list :
        result = True
    elif current_user not in  users_list and silent == True :
        result = False
    else:
        raise LoginException("Ooops, something wrong!!!")
    return result

username = input('Input your name: ')
password = input('Your password: ')
silent = bool(input('silent: ').title())
try:
    print(check_login(username, password, silent))
except LoginException as exc :
    print(exc)
finally:
    print("Stop".center(8,'*'))
    
