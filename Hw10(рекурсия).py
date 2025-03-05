# Задание 1: Поиск тайного сигнала

# def find_signal(room) -> bool:
#     '''Функция поиска строки 'сигнал' в аргументе функции.
#     Принимает строку или список. Возвращает False или True(в случае нахождения сигнала)'''     # НЕ ЗНАЮ как написать анотацию на 2 возможных типа(строка/лист)
#     if room == 'сигнал':
#         return True
  
#     elif isinstance(room, list):
#         for signal in room:          
#             if find_signal(signal):
#                 return 'мы нашли его'                
#     return False
    

# bunker = [
# 'тишина',
# ['тишина', ['тишина', ['тишина', 'сигнал'], 'тишина'], 'тишина'],
# ['тишина', ['тишина', ['тишина', ['тишина']]], 'тишина'],
# 'тишина'
# ]

# print(find_signal(bunker))             


# Задание 2: Сколько шагов до еды?


# count = 0  # глобальная переменная - счетчик для функции подсчета шагов. глобально,
# чтобы значение ее не обнулялось с кадым новым вызовом


# def count_steps_to_food(room:[str, list]) -> int:
#     '''Функция посчета шагов. Принимает строку или список строк. Подсчитывает кол-во шагов до строки
#     "еда".Возвращает кол-во шагов '''   
#     if room == 'еда':
#         return True       
#     elif isinstance(room, list):
#         global count             
#         for step in room:
#             if step == 'пусто':
#                 count += 1  
#             if count_steps_to_food(step):
#                 return count + 1
    
#     return 0


# bunker = [
# 'пусто',
# ['пусто', ['пусто', ['пусто', 'пусто', 'пусто'], 'пусто'], 'еда'],
# ['пусто', ['пусто', ['пусто', ['пусто']]]]
# ]

# print(count_steps_to_food(bunker))

# _____________________________
# Задание 3: Спасение робота

# steps_count = 0  # Опять глобальная переменная - счетчик для подсчет шагов. Глобальная, чтобы не обнулялся результат при вызове функции


# def rescue_robot(room:[str, list]) -> bool:
#     '''Функция поиска робота. Принимает строк или список строк. Возвращает True, если робот
#     найден в списке/строке, иначе возвращает False. Дополнительно: функция выведет кол-во шагов,
#       за которое робот был найден'''
    
#     if room == 'робот':
#         return True
#     elif isinstance(room, list):
#         for item in room:
#             global steps_count
#             if isinstance(item, str):
#                 steps_count += 1
#             if rescue_robot(item):
#                 return (True, steps_count) 
#     return False 
                
# bunker = [
# 'мусор',
# ['мусор', ['мусор', ['мусор', ['робот']], 'мусор'], 'мусор'],
# ['мусор', ['мусор', ['мусор', ['мусор']]]]
# ]

# robot, steps = rescue_robot(bunker)
# print(f'Робот найден: {robot}, за {steps} шагов') # True

# ______________________________
# Задание 4: Сбор топлива для выхода


# def count_fuel(room:[str, list]) -> int:
#     '''Функция ищет и считает все канистры с топливом.Принимает строку или список строк.
#     возвращает кол-во найденных канистр'''
#     if room == 'топливо':
#         return 1
#     if isinstance(room, list):
#         total_fuel_count = 0
#         for item in room:            
#             total_fuel_count += count_fuel(item)
#         return total_fuel_count
#     return 0

    
# bunker = [
# 'топливо',
# ['пусто', ['топливо', ['пусто', ['топливо']], 'пусто'], 'пусто'],
# ['топливо', ['пусто', ['топливо', ['топливо']]], 'пусто'],
# 'пусто'
# ]
# print(count_fuel(bunker)) #


# _________________________________________
# А теперь самое сладкое!!! СЛОВАРИ!(((
# Держись, капитан! 🚀 - это максимально ободряющий текст    
# 
#Задание 1: Найти портал в глубинах черной дыры


# def find_portal(space_map: dict) -> bool:
#     '''Функция поиска портала. Принимает словарь. Возвращает True, если 
#         в ЗНАЧЕНИЯХ ключей найден портал, иначе False'''
#     if isinstance(space_map, dict):
#         for key, value in space_map.items():
#             if value == 'портал':
#                 return True
#             elif find_portal(value):
#                 return True
#     return False


# space = {
#         "уровень 1": {
#             "уровень 2": {
#                 "уровень 3": {
#                     "уровень 4": {
#                         "аномалия": {
#                             "разлом": {
#                                 "надежда": "портал"
#                                        }
#                                      }
#                                   }
#                              }
#                          }
#                      }
#                 }

# print(find_portal(space))

# Задание 2: Починка гипердвигателя 🚀

# def collect_components(shipwreck: dict) -> list:
#     '''Функция поиска компонентов. Принимает словарь. Возвращает список компонентов'''
#     component_list = []
#     if isinstance(shipwreck, dict):
#         for key, value in shipwreck.items():
#             if key == 'компонент':
#                 component_list.append(value) 
#             elif isinstance(value, dict):
#                 component_list.extend(collect_components(value))
#     return component_list    


# shipwreck = {
# "зона 1": {
# "мусор": "ненужное",
# "зона 2": {
# "мусор": "ненужное",
# "зона 3": {
# "компонент": "плата",
# "зона 4": {
# "компонент": "двигатель",
# "зона 5": {
# "компонент": "конденсатор"
# }
# }
# }
# }
# }
# }
# print(collect_components(shipwreck))

# Задание 3: Найти энергию в гиперпространстве ⚡


def find_energy(data: dict) -> int:
    '''Функция суммирует энергию. Принимает словарь, возвращает сумму значений ключей "энергия" '''
    energy_sum = 0
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'энергия':
                energy_sum += value
            elif isinstance(value, dict):
                energy_sum += find_energy(value)
    return energy_sum

energy_data = {
"слой 1": {
"энергия": 10,
"слой 2": {
"аномалия": {
"энергия": 5,
"слой 3": {
"энергия": 2,
"слой 4": {
"энергия": 8
}
}
}
}
}
}
print(find_energy(energy_data))