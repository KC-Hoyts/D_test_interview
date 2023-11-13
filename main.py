#3. Имеется два списка разной длины. В первом содержатся ключи, а во втором — значения. Напишите функцию make_dict, которая создает словарь из этих ключей и значений. Если ключу не хватило значения, в словаре должно быть значение «None». Значения, которым не хватило ключей, следует игнорировать.
#10. Напишите функцию, объединяющую два списка в список кортежей. Если в одном из списков элементов меньше, то в результирующем списке на месте отсутствующих элементов должны быть строки «N/A». Подсказка: эту функцию можно написать в одну строку.
import os
print(os.listdir())

count = {}
opened_file = None
words = None
words_amount = {}
while True:

    print('Доступные команды:\n'
          '1 - Загрузить файл\n'
          '2 - Найти слово\n'
          '3 - Очистить результаты\n'
          '4 - Выйти\n')
    command = input("Введите команду: ")

    if command == '4':
        break
    elif command == '1':
        filename = input("Введите название файла: ")
        with open(f'check_file/files/text/{filename}.txt') as file:
            text = file.read()

        text = text.replace("\n", " ")
        text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace("—", "")
        text = text.lower()  # убираем верхний регистр
        words = text.split()
        print('words==:',words)
    elif command == '2':
        print(f'уникальные слова: {words_amount}')
        our_word = input('Введите слово: ')
        if our_word in words_amount:
            print('Вы уже искали это слово')
        else:
            if our_word not in words:
                print('Такого слова нет в тексте. Попробуйте другое слово')
            else:
                for word in words:
                    if word == our_word:
                        if our_word in words_amount:
                            words_amount[word] = words_amount[word]+1
                        else:
                            words_amount[word] = 1
                print(f'Слово "{our_word}" встречается в файле {words_amount[our_word]} раз')
    elif command == "3":
        words_amount = {}
    else:
        print('Некорректная команда. Введите корректную команду')


