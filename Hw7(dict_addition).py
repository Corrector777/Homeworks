phone_book = {'Иван':
              {'телефон': '+7992922929',
               'тэги': ['городской', 'мобильный', 'работа', 'друг']
               },
              'Коля':
              {'телефон': '+7992954554',
               'тэги': ['мобильный', 'работа', '222']
               }
              }

stop_words_set = {'выйти', '7', 'y', 'с', 'c'}

while True:
    print('Телефонная книга')
    print('Выберите дествие:\n\
    1. Добавить контакт\n\
    2. Обновить контакт(номер телефона/тэг)\n\
    3. Поиск по тегу\n\
    4. Удалить контакт\n\
    5. Показать все контакты\n\
    6. Выйти\n ')

    action_input = input('Введите: ').lower()
    match action_input:

        case 'добавить' | 'добавить контакт' | '1':
            name = input('Введите имя контакта: ').capitalize()
            if name in phone_book: # Введем проверку на наличие ключа в словаре. Если уже такой есть, то сообщение
                print('Такой пользователь уже сущетсвует! Обновите его данные или создайте иного пользователя\n')
            else:  # Если ключа нет, то добавляем всловарь значение
                number = input('Введите номер контакта: ').lower()
                tags = input('Введите нужные тэги через запятую или пробел: ').lower().split()            
                phone_book.update({name:   
                                   {'телефон': number,
                                    'тэги': tags                              
                                    }
                                   })
                print(f'<Пользователь {name} успешно добавлен>\n')
                
        case 'обновить' | 'обновить контакт' | '2':
            print('Вы можете обновить следующие контакты:')
            [print(f'- {k}') for k in phone_book]
            contact_select = input('Какой контакт вы хотите обновить(имя)?:').capitalize()
            if contact_select in phone_book:
                print('\nЧто хотите обновить(номер телефона/тэги)?\n')
                update_input = input('Введите вариант: \n').lower()
                match update_input:
                    case 'номер' | 'номер телефона' | 'телефон':
                        new_number = input('Введите новый номер телефона: ')
                        phone_book[contact_select]['телефон'] = new_number
                        print(f'\nНомер телефону успешно изменен на: {phone_book[contact_select]['телефон']}')
                    case 'тэг' | 'тэги':
                        print(f'У данного пользователя следующие тэги: {phone_book[contact_select]['тэги']}\n')
                        print('Хотите удалить тэг или добавить?\n')
                        tag_operation_input = input('Введите (добавить/удалить): ')
                        match tag_operation_input:
                            case 'добавить':
                                new_tags = input('Введите новые тэги: ').lower().split()
                                phone_book[contact_select]['тэги'].extend(new_tags)
                                print(f'\nНовый тэг для контакта <{contact_select}> успешно добавлен: {phone_book[contact_select]['тэги']}')
                            case 'удалить':
                                delete_tag = input('Введите тэг для удаления: ').lower()
                                try:
                                    phone_book[contact_select]['тэги'].remove(delete_tag)
                                    print(f'Тэг для контакта {contact_select} успешно удален: {phone_book[contact_select]['тэги']}\n')
                                except ValueError:
                                    print('Ошибка! Нет такого тэга')
                            case _:
                                print('\nОшибка! Такой команды нет\n')

                    case _:
                        print('Ошибка! Введите корректное значение\n')
            else:
                print('Такого пользователя в базе нет!\n')

        case 'поиск по тегу' | 'тэг' | '3':
            tag_input = input('Введите тэг для поиска: ').lower()
            tag_seach_list = []
            for name in phone_book:                
                if tag_input in phone_book[name]['тэги']:
                    tag_seach_list.append(name)                
            if tag_seach_list:
                tag_seach_dict = {name: phone_book[name]['телефон'] for name in tag_seach_list}
                print(f'По тэгу <{tag_input}> найдены пользователи:')
                [print(f'- {k}: телефон: {v}') for k, v in tag_seach_dict.items()]
                print()
            else:
                print('Внимание! Данный тэг не найден!\n')

        case 'удалить контакт' | '4':
            print('Вы можете удалить следующие контакты:')
            [print(f'- {k}') for k in phone_book]
            contact_select = input('Укажите имя контакта для удаления: ').capitalize()
            try:
                phone_book.pop(contact_select)
                print(f'Вы успешно удалили контакт: {contact_select}\n')
                print('В базе остались следующие контакты:' if phone_book.keys() else 'В базе пусто')
                [print(f'- {k}\n') for k in phone_book]   
            except KeyError:
                print('Ошибка! Такого контакта нет в базе')

        case 'показать' | 'все контакты' | '5':
            print('Давай взглянем кто у нас есть в базе:')
            for contact in phone_book:
                print(f'Имя: {contact}\n\
Номер телефона: {phone_book[contact]['телефон']}\n\
Тэги: {phone_book[contact]['тэги']}')
                print('_____________________________')
                                   
        case action if action in stop_words_set:
            names_count = len(phone_book)
            tags_count = (sum([len(phone_book[name]['тэги']) for name in phone_book])) # считаем кол-во тэгов в словаре с помощью генератора
            print(f'Статистика телефонной книги:\n\
Всего контактов: {names_count}\n\
Среднее количество тэгов: {tags_count / names_count}\n\
До свидания!')
            break
        case _:
            print('Введи корректную команду!')