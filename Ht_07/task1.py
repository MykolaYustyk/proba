#
#
# 1. Програма-банкомат.
#  Створити програму з наступним функціоналом:
#      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
#      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
#      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
#   Особливості реалізації:
#      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
#      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
#      - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
#   Особливості функціонала:
#      - за кожен функціонал відповідає окрема функція;
#      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
#      - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
#     - потім - елементарне меню типа:
#        Введіть дію:
#           1. Продивитись баланс
#           2. Поповнити баланс
#           3. Вихід
#
import json
class ValidationError(Exception) :
    pass
class OwerBalanceError(Exception) :
    pass

def start(user_name) :
    result = 0
    print('Привіт, ', user_name)
    print('_'*10)
    print('Введіть дію: \n', '1. Продивитись баланс\n', '2. Поповнити баланс\n', '3. Зняти кошти\n', '4. Вихід\n')
    result = int(input())
    return result

def validation(user_name, user_password) : 
    result = False
    current_user = []
    current_user.append(user_name)
    current_user.append(user_password)
    
    users_list = []
    with open ('users.txt', 'r') as users_file :
        users_as_list = users_file.readlines()
        for i in range(len(users_as_list)) :
            users_list.append((users_as_list[i])[:-1].split())
        users_list.append(users_as_list[-1].split())
        if current_user in users_list :
            result = True
        else : 
            raise ValidationError("Такого користувача немає")    
    return result

def view_balance(user_name) : 
     with open(user_name + "_balance.txt", 'r') as file_balance : 
                current_balance = file_balance.read()
                print("Ваш поточний баланс: ", current_balance)  
                
def add_balance(user_name, add_balance=True) :
    file_balance = open(user_name + "_balance.txt", 'r')
    current_balance = int(file_balance.read())
    file_balance.close()
    if add_balance :
        app_balance = int(input("На яку сумму Ви хочете поповнити Ваш рахунок? \n"))
    else: 
        app_balance = - int(input("Яку суму бажаєте зняти? \n"))
        if abs(app_balance)> current_balance :
            raise OwerBalanceError("Ви не можете зняти кошти більше, ніж поточний баланс.")
    with open(user_name + '_transaction.txt', 'a') as trans_file :
        json.dump({"transaction" : app_balance}, trans_file)
    current_balance += app_balance
    print("Ваш новий баланс: ", current_balance)
    file_balance = open(user_name + "_balance.txt", 'w')
    file_balance.write(str(current_balance))
    file_balance.close()
    
try :
    user_name = input("Введіть Ваше ім'я: ")
    user_password = input("Ваш пароль: ")
    while validation(user_name, user_password) :
        item = start(user_name)
        if item == 1:
            view_balance(user_name)
        elif item == 2 :
            add_balance(user_name)           
        elif item == 3 :
            add_balance(user_name, False)          
        else: 
            break        
        
except (ValidationError, OwerBalanceError) as err :
    print(err)
finally:
    print('Stop')
