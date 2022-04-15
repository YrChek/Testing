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


def check_document_existance(user_doc_number, def_documents):
    doc_founded = False
    for current_document in def_documents:
        doc_number = current_document['number']
        if doc_number == user_doc_number:
            doc_founded = True
            break
    return doc_founded


def get_doc_owner_name(user_doc_number, def_documents):
    # user_doc_number = input('Введите номер документа - ')
    print()
    doc_exist = check_document_existance(user_doc_number, def_documents)
    if doc_exist:
        for current_document in def_documents:
            doc_number = current_document['number']
            if doc_number == user_doc_number:
                return current_document['name']


def get_all_doc_owners_names(def_documents):
    users_list = []
    for current_document in def_documents:
        try:
            doc_owner_name = current_document['name']
            users_list.append(doc_owner_name)
        except KeyError:
            return False
    return set(users_list)


def remove_doc_from_shelf(doc_number, def_directories):
    for directory_number, directory_docs_list in def_directories.items():
        if doc_number in directory_docs_list:
            directory_docs_list.remove(doc_number)
            break
    return True


def add_new_shelf(new_shelf_number, def_directories):
    if not new_shelf_number:
        # new_shelf_number = input('Введите номер полки - ')
        pass
    if new_shelf_number not in def_directories.keys():
        def_directories[new_shelf_number] = []
        return new_shelf_number, True
    return new_shelf_number, False


def append_doc_to_shelf(doc_number, user_shelf_number, def_directories):
    add_new_shelf(user_shelf_number, def_directories)
    def_directories[user_shelf_number].append(doc_number)
    return def_directories[user_shelf_number]


def delete_doc(user_doc_number, def_documents, def_directories):
    # user_doc_number = input('Введите номер документа - ')
    doc_exist = check_document_existance(user_doc_number, def_documents)
    if doc_exist:
        for current_document in def_documents:
            doc_number = current_document['number']
            if doc_number == user_doc_number:
                def_documents.remove(current_document)
                remove_doc_from_shelf(doc_number, def_directories)
                return doc_number, True
    return user_doc_number, False


def get_doc_shelf(user_doc_number, def_documents, def_directories):
    # user_doc_number = input('Введите номер документа - ')
    doc_exist = check_document_existance(user_doc_number, def_documents)
    if doc_exist:
        for directory_number, directory_docs_list in def_directories.items():
            if user_doc_number in directory_docs_list:
                return directory_number
    return False


def move_doc_to_shelf(user_doc_number, user_shelf_number, def_directories):
    # user_doc_number = input('Введите номер документа - ')
    # user_shelf_number = input('Введите номер полки для перемещения - ')
    remove_doc_from_shelf(user_doc_number, def_directories)
    append_doc_to_shelf(user_doc_number, user_shelf_number, def_directories)
    return 'Документ номер "{}" был перемещен на полку номер "{}"'.format(user_doc_number, user_shelf_number)


def show_document_info(document):
    doc_type = document['type']
    doc_number = document['number']
    doc_owner_name = document['name']
    return '{} "{}" "{}"'.format(doc_type, doc_number, doc_owner_name)


def show_all_docs_info(def_documents):
    print('Список всех документов:\n')
    list_all_doc = []
    for current_document in def_documents:
        list_all_doc.append(show_document_info(current_document))
    return list_all_doc


def add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number,
                def_documents, def_directories):
    # new_doc_number = input('Введите номер документа - ')
    # new_doc_type = input('Введите тип документа - ')
    # new_doc_owner_name = input('Введите имя владельца документа- ')
    # new_doc_shelf_number = input('Введите номер полки для хранения - ')
    new_doc = {
        "type": new_doc_type,
        "number": new_doc_number,
        "name": new_doc_owner_name
    }
    def_documents.append(new_doc)
    append_doc_to_shelf(new_doc_number, new_doc_shelf_number, def_directories)
    return new_doc_shelf_number


def secretary_program_start(user_doc_number, user_shelf_number, new_shelf_number, new_doc_number, new_doc_type,
                            new_doc_owner_name, def_documents, def_directories):
    """
    ap - (all people) - команда, которая выводит список всех владельцев документов
    p – (people) – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    l – (list) – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    s – (shelf) – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    a – (add) – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
    имя владельца и номер полки, на котором он будет храниться.
    d – (delete) – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
    m – (move) – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
    as – (add shelf) – команда, которая спросит номер новой полки и добавит ее в перечень;
    q - (quit) - команда, которая завершает выполнение программы
    """
    print(
        'Вас приветствует программа помошник!\n',
        '(Введите help, для просмотра списка поддерживаемых команд)\n'
    )
    while True:
        user_command = input('Введите команду - ')
        if user_command == 'p':
            owner_name = get_doc_owner_name(user_doc_number, def_documents)
            print('Владелец документа - {}'.format(owner_name))
        elif user_command == 'ap':
            uniq_users = get_all_doc_owners_names(def_documents)
            print('Список владельцев документов - {}'.format(uniq_users))
        elif user_command == 'l':
            all_doc = show_all_docs_info(def_documents)
            for doc in all_doc:
                print(doc)
        elif user_command == 's':
            directory_number = get_doc_shelf(user_doc_number, def_documents, def_directories)
            print('Документ находится на полке номер {}'.format(directory_number))
        elif user_command == 'a':
            print('Добавление нового документа:')
            doc_shelf_number = add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_shelf_number,
                                           def_documents, def_directories)
            print('\nНа полку "{}" добавлен новый документ:'.format(doc_shelf_number))
        elif user_command == 'd':
            doc_number, deleted = delete_doc(user_doc_number, def_documents, def_directories)
            if deleted:
                print('Документ с номером "{}" был успешно удален'.format(doc_number))
            else:
                print('Документ с номером "{}" отсутствует в перечне'.format(doc_number))
        elif user_command == 'm':
            shelf = move_doc_to_shelf(user_doc_number, user_shelf_number, def_directories)
            print(shelf)
        elif user_command == 'as':
            shelf_number, added = add_new_shelf(new_shelf_number, def_directories)
            if added:
                print('Добавлена полка "{}"'.format(shelf_number))
        elif user_command == 'help':
            print(secretary_program_start.__doc__)
        elif user_command == 'q':
            break


if __name__ == '__main__':
    secretary_program_start('1', '1', '1', '1', '1', '1', documents, directories)
