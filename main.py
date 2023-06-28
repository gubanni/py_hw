#Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
#Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию. 
#Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, а для директорий размер файлов в 
#ней с учётом всех вложенных файлов и директорий.

from create_file_txt import create_file_txt
from txt_to_json import txt_to_json
from create_file_json import  func
from json_to_csv import json_to_csv
from csv_to_json import csv_to_json
from directory_reference import directory_reference
import csv
from pathlib import Path

if __name__ == '__main__':

    create_file_txt('data.txt', 'w')                          #создание файла с расширением txt с данными:  рандомное слово: рандомное значение
    for _ in range(10):
        create_file_txt('data.txt', 'a')

    txt_to_json('data.txt', 'data.json')                      #создание из файла txt нового файла json Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.

    func('data1.json')                                         #запись в json файл данных: имени, Id и уровня. Id -  ключ для имени. Все идентификаторы уникальны независимо от уровня доступа.

    json_to_csv('data1.json', 'data.csv')                     #перенос данных из json файла в файл csv

    with open('data.csv') as file_obj:                        # чтение csv data2
      
        reader_obj = csv.reader(file_obj)
      
   
        for row in reader_obj:
            print(row)

    csv_to_json('data.csv', 'data2.json')                     #запись из csv файла  в json файл, где каждая строка csv файла представлена как отдельный json словарь

    directory_reference(Path(Path.cwd()))                       #спрвавочник по содержимому директория: (наименование объекта, тип объекта в директории, размер объекта, родительский директорий объекта)