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


def person(number_doc='10006'):
    for my_string in documents:
        for my_key, my_value in my_string.items():
            if number_doc in my_value:
                return my_string['name']


def shelf(number_doc='10006'):
    for my_key, my_value in directories.items():
        if number_doc in my_value:
            return my_key
    else:
        return False


def list_command():
    for my_string in documents:
        for my_key, my_value in my_string.items():
            print(my_value)


def add_command(type_doc='passport', number_doc='2207 876234', name_usr='Василий Гупкин', number_shelf='1'):
    documents.append({'type': type_doc, 'number': number_doc, 'name': name_usr})
    directories[number_shelf].append(number_doc)
    return documents, directories


def chek_shelf(number_shelf='1'):
    if number_shelf in directories.keys():
        return True
    else:
        return False


def del_command_documents(number_doc='10006'):
    for my_string in documents:
        if number_doc in my_string.values():
            documents.remove(my_string)
            return documents

    else:
        return 'Нечего удалять!'


def del_command_directories(number_doc='10006'):
    for my_key, my_value in directories.items():
        if number_doc in my_value:
            my_value.remove(number_doc)
            return directories
    else:
        return 'Нечего удалять!'


def move_command(number_doc='10006', number_shelf='1'):
    for my_key, my_value in directories.items():
        if number_doc in my_value:
            my_value.pop(my_value.index(number_doc))

    directories[number_shelf].append(number_doc)
    return directories


def add_shelf_comand(number_shelf='99'):
    directories[number_shelf] = []
    return directories


if __name__ == '__main__':

    while True:

        my_command = input('Введите команду: ')

        if my_command == 'p':
            number_doc = input('Введите номер документа: ')
            if shelf(number_doc):
                print(person())
            else:
                print('Такого номера не существует')

        elif my_command == 's':
            number_doc = input('Введите номер документа: ')
            if shelf(number_doc):
                print(shelf(number_doc))
            else:
                print('Такого номера не существует')

        elif my_command == 'l':
            print(list_command())


        elif my_command == 'a':

            type_doc = input('Введите тип документа: ')
            number_doc = input('Введите номер документа: ')
            name_usr = input('Введите Ваше имя и фамилию: ')
            number_shelf = input('Введите номер полки для хранения дела: ')

            if chek_shelf(number_shelf=number_shelf):
                add_command(type_doc=type_doc, number_doc=number_doc, name_usr=name_usr, number_shelf=number_shelf)
                print(documents)
                print(directories)
            else:
                print('Такой полки не существует: ')

        elif my_command == 'd':
            number_doc = input('Введите номер документа: ')
            print(del_command_documents(number_doc))
            print(del_command_directories(number_doc))


        elif my_command == 'm':
            number_doc = input('Введите номер документа: ')
            number_shelf = input('Введите номер полки для хранения дела: ')

            if shelf() and chek_shelf():
                print(move_command(number_doc=number_doc, number_shelf=number_shelf))

        elif my_command == 'as':
            number_shelf = input('Введите номер полки для хранения дела: ')

            if shelf() != 'True':
                print(add_shelf_comand(number_shelf=number_shelf))
