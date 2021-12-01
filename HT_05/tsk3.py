# 3. На основі попередньої функції створити наступний кусок кода:
#  а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
#   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
#      Name: vasya
#      Password: wasd
#      Status: password must have at least one digit
#      -----
#      Name: vasya
#      Password: vasyapupkin2000
#      Status: OK
#   P.S. Не забудьте використати блок try/except ;)
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

users_list = [['user1', 'password1'],
              ['us', 'password2'],
              ['user3', 'pass1'],
              ['user4', 'pass'],
              ['user5aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaapopo11111123333', 'password']]
status =''
for i in range(len(users_list)):
    try:
         name = users_list[i][0]
         password = users_list[i][1]
         if user_validation(name, password) == True : 
             status = "Ok"
       
    except (NameValidationException, PassValidationException) as exc:
        status = exc
    finally:
         print('Name: ', name)
         print('Password: ', password)
         print('Status: ', status)