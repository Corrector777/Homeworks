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
#         result_dict = {dwarf: random.choice(range(10)) for dwarf in dwarf_list}  # создадим словарь ключ-имя, значение- случ цифра от 0 до 9  
#         winner = max(result_dict, key=result_dict.get) # поиск ключа с максимальным значением
#         # print(result_dict)  # проверочный принт
#         yield f'Раунд {current_round}: Лидер - {winner} ({result_dict[winner]} алмазов) '
#         current_round += 1


# winner = winner_dwarf(dwarfs)
# for i in range(4):
#   print(next(winner))