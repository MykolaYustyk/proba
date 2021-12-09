#
#    2. Написати функцію, яка приймає два параметри: ім'я файлу та кількість символів.
#   На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу.
#   Кількість символів в блоках - та, яка введена в другому параметрі.
#   Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша,
#   ніж є в файлі (наприклад, файл із двох символів і треба вивести по одному символу,
#   то що виводити на місці середнього блоку символів?)
#   В репозиторій додайте і ті файли, по яким робили тести.
#  Як визначати середину файлу (з якої брать необхідні символи) - кількість символів поділити
#   навпіл, а отримане "вікно" символів відцентрувати щодо середини файла і взяти необхідну кількість.
#   В разі необхідності заокруглення одного чи обох параметрів - дивіться на свій розсуд.
import math

class ValueCountError(Exception) :
    pass
class NegativeZeroError(Exception) :
    pass
def print_symbols_in_file(file_name, count_symbols):
    result_list = []
    file = open(file_name, 'r')
    str = file.read()
    print('Input file is:\n',str)
    if 0 < count_symbols  <= len(str) :
        result_list.append(str[:count_symbols])
        center_of_file = round(len(str)/2)
        result_list.append(str[center_of_file - math.floor(count_symbols/2):center_of_file + math.ceil(count_symbols/2)])
        result_list.append(str[-count_symbols:])
        print(result_list)
    elif count_symbols > len(str) :
        raise ValueCountError("Error! Count of symbols bigger them length of the string.")
    else: 
        raise NegativeZeroError('Error! Count of symbols must be positive integer.')   
    file.close()
    return

int_file = input("Name of input file: ")
count_symbols = int(input("Count of symbols which you want print "))
try : 
    print_symbols_in_file(int_file, count_symbols)
except (ValueCountError, NegativeZeroError) as err :
    print(err)
finally:
    print('Stop'.center(20, '*'))       
