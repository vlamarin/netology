import datetime
import sys
from contextlib import contextmanager

@contextmanager
def timer():
    try:
        time_1 = datetime.datetime.now()
        print(f'{time_1}: Время запуска кода.')
        yield #print(f'{datetime.datetime.now()}: Время окончания работы кода\n')
    finally:
        exc_type, exc_val, exc_tb = sys.exc_info()
        if exc_type is not None:
            print(f'{datetime.datetime.now()}: Error: {exc_val}.')
        time_2 = datetime.datetime.now()
        print(f'{time_2}: Время окончания работы кода.\nПотрачено времени на выполнение кода: {time_2 - time_1}.')

if __name__ == '__main__':
    with timer():
        documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]

        directories = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': []
        }

        try:
            for document in documents:
                test_number = document["number"]
                test_mame = document["name"]

        except:
            print(f'Внимание! У документа под номером {test_number} нет данных о владельце!')


        def get_name_by_number():
            input_number = input('Введите номер документа: ')
            for document in documents:
                if input_number == document['number']:
                    name = document['name']
                    print(f'Владелец документа с номером "{input_number}" - {name}.')
                    return
            print(f'Домента с номером "{input_number}" нет в каталоге.')


        # get_name_by_number()

        def get_number_of_directory():
            input_number = input('Введите номер документа: ')
            for directory in directories.items():
                if list(directory)[1].count(input_number) == 1:
                    print(f'Документ с номером "{input_number}" храниться на полке №{list(directory)[0]}.')
                    return
            print(f'Домента с номером "{input_number}" нет в каталоге.')


        # get_number_of_directory()

        def get_all():
            for document in documents:
                type_doc = document['type'].capitalize()
                number = document['number']
                name = document['name']
                print(f'{documents.index(document) + 1}) {type_doc} "{number}" "{name}"')


        # get_all()

        def add_new_doc():
            new_doc = {}
            intput_type = input('Введите тип документа: ')
            intput_number = input('Введите номер документа: ')
            intput_1_name = input('Введите имя владельца: ')
            intput_2_name = input('Введите фамилию владельца: ')
            intput_number_of_directory = input('Введите номер полки, на которой разместить документ: ')
            new_name = intput_1_name.capitalize() + ' ' + intput_2_name.capitalize()
            new_doc["type"] = intput_type
            new_doc["number"] = intput_number
            new_doc["name"] = new_name
            if intput_number_of_directory in directories.keys():
                directories[intput_number_of_directory].append(intput_number)
                documents.append(new_doc)
                print(f'Документ с номером "{intput_number}", добавлен на полку №{intput_number_of_directory}.')
            else:
                print(f'Полки с номером "{intput_number_of_directory}" не существует!')


        # add_new_doc()

        def help_for_user():
            for_print = '1) Нажмите "p", чтобы по номеру документа узнать имя человека, которому он принадлежит.\n\
            2) Нажмите "s", чтобы по номеру документа узнать номер полки, на которой он находится.\n\
            3) Нажмите "l", чтобы вывести на экран список всех документов.\n\
            4) Нажмите "a", чтобы добавит новый документ в каталог и в перечень полок.\n\
            5) Нажмите "q", чтобы выйти из программы.'
            print(for_print)


        # help_for_user()

        def main():
            while True:
                user_input = input('Введите команду (для справки, нажмите "h"): ').lower()
                if user_input == 'h':
                    help_for_user()
                elif user_input == 'p':
                    get_name_by_number()
                elif user_input == 's':
                    get_number_of_directory()
                elif user_input == 'l':
                    get_all()
                elif user_input == 'a':
                    add_new_doc()
                elif user_input == 'q':
                    print('Работа завершена.')
                    break


        main()