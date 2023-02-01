def main_menu():
    commands = ['Показать все контакты',
                'Открыть файл',
                'Сохранить файл',
                'Новый контакт',
                'Изменить контакт',
                'Удалить контакт',
                'Найти контакт',
                'Выйти из программы']
    print('\nВыберите пункт меню: ')
    for i in range(len(commands)):
        print(f'\t{i+1}. {commands[i]}')
    user_input = int(input('\nВведите пункт меню: '))
    return user_input


def error_enter():
    return print('Введите корректное значение (1-8): ')


def show_contacts(phone_book: list):
    if len(phone_book) > 0:
        for item in phone_book:
            print(f'{item[0]:20} {item[1]:10} ({item[2]})')
    else:
        print('Телефонная книга пустая или не загружена')


def load_success():
    print('Телефонная книга загружена успешно')


def save_success():
    print('Телефонная книга сохранена успешно!')


def new_contact():
    name = input('Введите Имя и Фамилию контакта: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий к контакту: ')
    return name, phone, comment


def find_contact():
    search = input('Введите искомое значение: ')
    return search


def delete_contact():
    cont_del = input('Какого контакта вы хотите удалить? ')
    return cont_del


def info_fall_del():
    print(f'Контакт успешно удалён!')


def info_cha_na():
    cha_na = input('Введите имя контакта которого хотите изменить: ')
    return cha_na


def change_cont():
    new_cha = input('Введите новое имя: ')
    new_cha2 = input('Введите новый номер: ')
    new_cha3 = input('Введите новый комментарий: ')
    return new_cha, new_cha2, new_cha3
