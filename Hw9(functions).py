# Часть 1. Подготовка к запуску
def greet_commander(name='Космический исследователь', greeting="Добро пожаловать на борт") -> str:
    '''Функция приветсвия коммандира. На вход принимает 2 аргумента(тип- строка). 
        Возращает строку с приветствием'''
    return f'{greeting}, {name}! Готовьтесь к запуску космического корабля.'


print(greet_commander(greeting='Привет', name='Jack'))


# Часть 2. Навигация через звездный лабиринт
def navigate_space(*args: str, bonus=0, penalty=0) -> int:
    '''Функция вычисляет и возвращает навигационный бал. На входи принимает неопределенное кол-во позиционных аргументов и 2 именованных с дефолтным значением'''
    navigation_result = 0  # переменная для подсчета баллов согласно маневрам
    penalty_count = 0  # Подсчет кол-ва штрафных маневров
    for direction in args:  # Перебираем циклом все значения args 
        match direction.lower():  # для каждого из из значений args отлавливаем совпадения выражений
            case 'вперед' | 'назад':
                navigation_result += 15  
            case 'налево' | 'направо':
                navigation_result -= 7
                penalty_count += 1        
    final_result = navigation_result - penalty_count * penalty + bonus   # Итоговый подсчет баллов 
    return final_result


# print(navigate_space('Вперед', 'Назад', 'Назад', 'налево', 'направо', 'вперед', penalty=10))
# print(navigate_space('Назад', 'назад', 'налево', 'налево', 'направо', 'направо', 'направо', bonus=5))
print(navigate_space('Вперед', 'Назад', 'Назад', 'налево', 'направо', 'вперед', penalty=10, bonus=400))


# Часть 3. Битва с инопланетным кораблём
def battle_alien(ship_attack=0, alien_defence=0, ship_health=100, alien_health=120) -> tuple[int, int, str]:
    '''Функция вычисляет урон в битве между своим и инопланет кораблями. На вход принимает
    4 именованных необязательных аргумента(со значениями по умолчанию). Возвращает кортеж из 3х значений(число,число, строка)'''
    my_ship_damage = ship_attack - alien_defence // 2
    if my_ship_damage <= 0:
        my_ship_damage = 1
    alien_ship_damage = 20
    my_ship_hp = ship_health - alien_ship_damage
    alien_ship_hp = alien_health - my_ship_damage
    message = ''
    if alien_ship_hp <= 0:
        message = "Инопланетяне повержены! Космический мир спасён!"
    elif my_ship_hp <= 0:
        message = "Ваш корабль уничтожен... миссия провалена."
    else:
        message = "Битва продолжается..." 
    return (my_ship_hp, alien_ship_hp, message)

    
ship_hp, alien_hp, result = battle_alien(150, 60)
print(f"Здоровье корабля: {ship_hp}")
print(f"Здоровье инопланетного корабля: {alien_hp}")
print(result)