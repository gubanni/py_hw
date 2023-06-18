# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

pathToFile = r'C:\users\Evgeny\hw5_1.py'


def cortezhOfThree(abs_path):
    list = abs_path.split(chr(92))
    last_elem = list[-1].split('.')
    path = ""
    i = 0
    while i < len(list)-1:
        path = path + list[i]+chr(92)
        i+=1
    name = last_elem[0]
    expension = last_elem[1]
    return path, name, expension


print(cortezhOfThree(pathToFile))