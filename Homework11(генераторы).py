import random

# # Задание 1: Загадочный сундук

# items = ['меч', 'щит', 'зелье', 'ключ']
# riddles = ['Острое и блестящее', 'Защитит от удара', 'Восстанавливает силы',
# 'Открывает любые двери']


# pairs_list = []
# for i in range(len(items)):
#     pairs_list.append((items[i], riddles[i]))
# random.shuffle(pairs_list)
# iterator = iter(pairs_list)

# try:
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
# except StopIteration:
#     print("Сундук пуст, поиск окончен!")


# Задание 2: Генератор магических заклинаний
# magic_symbols = ['@', '#', '%', '&', '*']
# times = 5
# start_word = 'магия'


# def magic_spell(start_word):
#     '''Генератор слов. Принимает стартовое слово в виде строки.
#        перемешивает буквы слова, добавляет спецсимвол и возвращает полученное значение 
#      в виде новой строки'''
#     current_word = start_word  # задаем значение текущего слова для дальнейшего изменения  
#     while True:    # Использую бесконечный цикл для генератора, так как кол-во вызовов генератора 
#                     #определяется циклом вызова генератора. При этом возможность случайной генерации при 
#                     # увеличении числа вызовов генератора не останавливалась
#         word_symb = [symb for symb in current_word]  # создаем список символов из стартовой строки
#         random.shuffle(word_symb)  # Перемешиваем символы
#         shuffled_word = ''.join(word_symb) # сохраняем новую строку из перемешанных символов
#         new_spell = shuffled_word + random.choice(magic_symbols)  # добавляем спецсимвол
#         current_word = shuffled_word # обновляем значение текущего слова для последующих итераций
#         yield new_spell
        

# my_gen = magic_spell(start_word)
# for _ in range(times):    
#     print(next(my_gen))

# Задание 3: Гномы-шахтёры (соревнование)
# dwarfs = ['Бофур', 'Кили', 'Ори']


# def winner_dwarf(dwarf_list, current_round=1):
#     '''Генератор определения победителя. Принимает список игороков.
#        возвращает имя победителя и кол-во собранных алмазов'''
#     while True:
#           result_dict = {dwarf: random.choice(range(10)) for dwarf in dwarf_list}  # создадим словарь ключ-имя, значение- случ цифра от 0 до 9  
#           winner = max(result_dict, key=result_dict.get) # поиск ключа с максимальным значением
#           # print(result_dict)  # проверочный принт
#           yield f'Раунд {current_round}: Лидер - {winner} ({result_dict[winner]} алмазов) '
#           current_round += 1


# winner = winner_dwarf(dwarfs)
# for i in range(4):
#     print(next(winner))


# # Задание 4: Лабиринт с секретными порталами
# # portal_positions = {3: 7, 6: 2, 10: 15} # ключ — шаг, значение — куда
# # steps_total = 12


# def portal_search(portal_positions):
#     count = 0
#     while True:
#         count += 1
#         if count in portal_positions.keys():
#             yield f'Шаг {count} портал! Перенос на шаг {portal_positions[count]}'
#         else:
#             yield f'Шаг {count} безопасен'


# portal_gen = portal_search(portal_positions)            
# for _ in range(steps_total):
#   print(next(portal_gen))

# Задание 5: Финальный пароль (генератор с send и throw)
final_password = 'итератор'


def check_password(password, attemps):
    attemps_left = attemps  # задаем остаток попыток
    ''' ARGS: истинный пароль(password), кол-во попыток
        - Принимает варианты  паролей пользователя с помощью send().
        - Проверяет совпадает ли пароль пользователя с истинным паролем(password)
        - Отлавливает возможные ошибки,которые мы отправим в генератор с помощью throw()
        - Подсчитывает кол-во попыток
        Генератор возвращает True,если пароль пользователя верен, иначе ничего
        '''    
    while True:      
        try:
            current_password = yield  # ожидаем ввод пароля от пользователя
            if current_password == password:  # если пароль равен искомому(верный)
                print('Ура! Пароль верный! Стоп игра')
                yield True  # возвращаем true для внешней логики и останавливаем генератор
                break
            else:
                attemps_left -= 1  # если пароль неверный, уменьшаем кол-во попыток
                if attemps_left > 0:  # если попытки еще есть, то выводим сообщение
                    print(f'Пока неверно. Осталось попыток: {attemps_left} ')  
        except ValueError:  # отклавливаем throw() и завершаем работу генератора
            print(f'Неверных попыток: {attemps}! выключаюсь')


max_attempts = 3  # задаем кол-во попыток
password_gen = check_password(final_password, max_attempts)  # создаем экземпляр генератора
next(password_gen)  # первый вызов генератора(пробуждение)

'''Цикл для того, чтобы динамически вводить пароли, а также автоматически 
каждые n попыток вбрасывать ошибку в генератор'''
for i in range(10):
    if i == max_attempts:  # Если номер текущей итерации равен заданному пределу попыток,
        password_gen.throw(ValueError)   # Выбрасываем ошибку в генератор и остановливаем данный цикл
        break
    else:  # иначе:
        new_password = input("Введи пароль: ")   # вводим пароль и получаем ответ от генератора
        if password_gen.send(new_password):   # Если вернулось True, прекращаем данный цикл     
            break