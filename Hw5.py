from collections import namedtuple

# treasures = [(10, 15, "Золотая маска"), (5, 20, "Древний свиток"), (25, 30,
# "Сапфировый камень")]



# 1. Квест «Сокровища Древнего Храма»
# Цель: Практика работы с кортежами, индексами, распаковкой.

#Выводит координаты и артефакты
# def treasures_data(a):
#     res = ''
#     for treasure in a:
#         x, y, name = treasure
#         res += f'по кординатам: <{x}:{y}> находится сокровище: {name}\n'
#     return res


#Находит артефакт по заданным координатам
# def treasure_search(x_coord, y_coord):
#     for treasure in treasures:
#         x, y, name = treasure
#         if x_coord == x and y_coord == y:
#             return name
        

# создает новый список артефактов и добавляет в него новый артефакт
# def add_treasure(x, y, name):
#     new_treasures_list = treasures.copy() 
#     new_treasure = x, y, name    
#     new_treasures_list.append(new_treasure)
#     return new_treasures_list


# print(treasures_data(treasures))  # выводим все сокровища из списка
# print(treasure_search(5, 20))  #  поиск сокровища по координатам
# print(add_treasure(3, 6, "Клинок"))  # добавляет новое сокровище в список сокровищ(новый список)


# 2. Магический портал
# Цель: Практика работы с неизменяемостью кортежей, генерацией новых кортежей.

# portals = [("Синий", 100, "Лес"), ("Красный", 200, "Замок"), ("Зелёный",
# 150, "Озеро")]
# new_portal_lst = []


# создание нового портала с измененными параметрами изначального портала
# def create_new_portal(old_portal, color=None, power=None, place=None):
#     old_color, old_power, old_place = old_portal
#     color = old_color if color is None else color
#     power = old_power if power is None else power
#     place = old_place if place is None else place
#     new_portal = color, power, place    
#     return new_portal


#Поиск самого мощного портала
# def seach_max_power_portal(portals_list):
#     max_power = 0
#     max_power_portal = tuple()
#     for portal in portals_list:
#         color, power, place = portal
#         if power > max_power:
#             max_power = power
#             max_power_portal = color, power, place
#     return f'самый мощный портал: {max_power_portal}'


#Создание портала с удвоенной мощностью
# def double_power(portal):
#     color, power, place = portal
#     double_power = power * 2
#     doublled_power_portal = color, double_power, place 
#     return doublled_power_portal


#проверка, если ли портал в указанном месте
# def portal_place_check(portal, check_place=None):  #check_place специально задаем необязательным аргументом
#     color, power, place = portal
#     check_result = ''
#     if check_place and check_place.lower() == place.lower():
#         check_result += f'Успех! вы нашли портал: {portal}'
#     else:
#         check_result += f'Ой-ей!!В данном месте портала нет'
#     return check_result

# print(portals[0])  #первый элемент списка
# print(create_new_portal(portals[0], power=1000, place='Солнце')) # Новый портал
# print(seach_max_power_portal(portals))  # Ищем самый мощный портал
# print(double_power(portals[0]))  # удваиваем силу портала
# print(portal_place_check(portals[0], 'Лес'))  # проверяем наличие портала в заданном месте



# 3.Арена Гладиаторов
# Цель: Практика сортировки кортежей, работы с индексами.

# gladiators = [("Максимус", 80, 60), ("Спартак", 90, 50), ("Цезарь", 85, 70)]


# поиск самого сильного гладиатора
# def seach_most_powerfull_gladiator(gladiators_list):
#     max_power = 0
#     most_powerfull_name = ''
#     for gladiator in gladiators_list:
#         name, power, agility = gladiator
#         if power > max_power:
#             max_power = power
#             most_powerfull_name = name
#     return f'самый сильный гладиатор: {most_powerfull_name}'


# определение победителя(по сумме силы и ловкости)
# def determinate_winner(gladiators_list):
#     max_sum_power_agility = 0
#     winner_name = ''
#     for gladiator in gladiators:
#         name, power, agility = gladiator
#         sum_power_agility = power + agility
#         if sum_power_agility > max_sum_power_agility:
#             max_sum_power_agility = sum_power_agility
#             winner_name = name
#     return f'победил гладиатор: {winner_name}'
    

# сортирует бойцов по силе в порядке убывания.
# def sort_gladiators(gladiators_list):
#     gladiators_list.sort(reverse=True, key=lambda x: x[1])
#     return gladiators_list

# print(seach_most_powerfull_gladiator(gladiators))  #самый сильный гладиатор
# print(determinate_winner(gladiators_list=gladiators)) # выводим победителя
# print(sort_gladiators(gladiators_list=gladiators)) # сортируем список по силе в порядке убывания


# 4. Космическая Экспедиция
# Цель: Практика работы с кортежами в словарях, поиска по ключам.

# planets = {
# (5.97, 15, 0): "Земля",
# (1.89, -110, 778): "Юпитер",
# (0.33, 167, 57): "Меркурий"
# }

# Самая горячая планета
# def hottest_planet(planets_dict):
#     sorted_planets_list = sorted(planets_dict, reverse=True, key=lambda x: x[1])
#     return f'Самая горячая планета: {planets_dict[sorted_planets_list[0]]}'


# Поиск планеты поо характеристикам
# def seach_planet(characteritics_tuple):
#     if characteritics_tuple not in planets:
#         raise ValueError(f'Планеты с характеристиками: {characteritics_tuple} в базе нет')
#     else:        
#         return f'Искомая планета: {planets[characteritics_tuple]}'


# Добавит новую планету, не изменяя исходный словарь (создавая новый).
# def new_planet(characteristic_tuple, name):
#     new_planets = planets.copy()
#     new_planets[characteristic_tuple] = name
#     return new_planets


# print(hottest_planet(planets_dict=planets))  #горячая планета

# try:
#     print(seach_planet((5.97, 15, 9))) # Ищем планету по ключу, обрабатывая KeyError
# except ValueError as e:
#     print(e)

# new_planet_characteristics = (3.33, 3, 4)   # Новая планета
# print(new_planet(new_planet_characteristics, 'HHH'))


# 5. Легенда о Драконе
# Цель: Практика использования namedtuple и работы с кортежами.

Dragon = namedtuple("Dragon", ["name", "level", "hp"])
dragon1 = Dragon('Залетный', 80, 1)
dragon2 = Dragon('Огненный', 33, 8)
dragon3 = Dragon('Дымный', 59, 44)
dragon4 = Dragon('Гнусавый', 77, 9)
dragon5 = Dragon('Лихой', 44, 99)
dragons_list = [dragon1, dragon2, dragon3, dragon4]


# Определим самомго сильного дракона
# def most_powerfull(dragons_lst):
#     max_level = 0
#     most_powerfull_name = ''
#     for dragon in dragons_list:
#         if dragon.level > max_level:
#             max_level = dragon.level
#             most_powerfull_name = dragon.name
#     return most_powerfull_name


# Определит, кто из драконов побежден (если hp <= 0).
def dragon_defeated(dragons_lst):
    dragon_defeated_name = []
    for dragon in dragons_list:
        if dragon.hp <= 0:
            dragon_defeated_name.append(dragon.name)
        
    return dragon_defeated_name if dragon_defeated_name else "пока нет побежденных"


# def add_new_dragon(new_dragon):
#     new_dragon_list = dragons_list[:]
#     new_dragon_list.append(new_dragon)
#     return new_dragon_list


# print(most_powerfull(dragons_lst=dragons_list)) # Самый сильный
print(dragon_defeated(dragons_lst=dragons_list)) # Побежденный
# print(add_new_dragon(dragon5)) # Новый дракон

