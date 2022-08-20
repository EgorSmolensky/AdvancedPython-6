documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def take_command():
    message = """Вам доступны следующие команды: 
          p - поиск человека по номеру его документа,
          s - поиск полки, на которой хранится документ,
          l - вывод списка всех документов, хранящихся в архиве,
          a - добавление нового документа в архив,
          d - удаление документа из архива,
          m - перемещение документа на другую полку,
          as - добавление новой полки,
          exit - завершеие работы архива"""
    print(message)

    commands = {
        'p': search_people,
        's': find_sheil,
        'l': print_list,
        'a': add_document,
        'd': delete_document,
        'm': move_document,
        'as': add_sheil
    }

    command = input('Введите комманду: ')
    while command != 'exit':
        if command in commands:
            commands[command]()
            command = input('\nВведите следующую комманду (help - показать список комманд): ')
        elif command == 'help':
            print(message)
            command = input('\nВведите следующую комманду: ')
        else:
            command = input('Неверная комманда. Повторите ввод: ')


def search_people():
    doc_num = input('Введите номер документа: ')
    doc_name = None
    for document in documents:
        if document['number'] == doc_num:
            doc_name = document['name']
            break
    if doc_name is None:
        print('Документ с таким номером отсутствует.')
    return doc_name


def find_sheil():
    doc = input('Введите номер документа: ')
    sheil_num = None
    for number in directories:
        if doc in directories[number]:
            sheil_num = number
            break
    if sheil_num is None:
        print('Документ с таким номером отсутствует.')
        return
    return 'Документ находится на полке № ' + sheil_num


def print_list():
    for document in documents:
        print(document['type'], ' "', document['number'], '" "', document['name'], '"', sep='')


def add_document(doc_type, doc_num, doc_name):
    sheil_num = input('Введите номер полки для хранения: ')
    if sheil_num not in directories:
        print('Такой полки не существует. Документ не добавлен')
        return False
    documents.append({"type": doc_type, "number": doc_num, "name": doc_name})
    directories[sheil_num].append(doc_num)
    print('Документ добавлен')
    return True


def delete_document():
    doc_num = input('Введите номер документа: ')
    sheil_num = None
    for number in directories:
        if doc_num in directories[number]:
            sheil_num = number
            break
    if sheil_num is None:
        print('Документ с таким номером отсутствует.')
        return False
    for document in documents:
        if document['number'] == doc_num:
            break
    documents.remove(document)
    directories[sheil_num].remove(doc_num)
    print('Документ удален')
    return True


def move_document():
    doc = input('Введите номер документа: ')
    sheil_num = None
    for number in directories:
        if doc in directories[number]:
            sheil_num = number
            break
    if sheil_num is None:
        print('Документ с таким номером отсутствует.')
        return
    sheil = input('Введите номер полки для перемещения: ')
    while sheil not in directories:
        sheil = input('Такой полки не существует. Введите номер полки: ')
    directories[sheil_num].remove(doc)
    directories[sheil].append(doc)


def add_sheil():
    num = input('Введите номер новой полки: ')
    if num in directories:
        print('Полка с таким номером уже существует')
        return False
    directories[num] = []
    print('Полка добавлена')
    return True


if __name__ == '__main__':
    take_command()



