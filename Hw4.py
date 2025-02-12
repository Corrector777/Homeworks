import re  # так как при вводе есть и пробелы и запятые, то решил через регулярное
import random 
items_list = ['ключ', 'свеча', 'старый свиток', 'меч']
selected_items = []
finish_anwser = ['готов', 'поехали', 'go', 'да', 'yes', 'y', 'н']
game_flag = True
intro_flag = True
wizard_flag = False
bridge_flag = False
final_flag = False


# class InvalidItemError(Exception):  # создадим класс для собственной ошибки
#     pass 


# Функция для определения пересекающего множества между изначально заданным списком предметов(items_list) и
# введенным пользователем списком. Функция сравнивает множества и возвращает список пересекаемых элементов
def return_matches(a, b):  
    return list(set(a) & set(b))


# Функция для  определения ответа на мосту с использованием функции random.choise(случайный выбор).
# Дабы не писать много одиннакового кода на if
def anwser_func(a):
    if a == '2':
        return random.choice(('1', '3'))
    else:
        return a


print('Начнем игру! У нас в ассортименте:', ', '.join(items_list))

while game_flag:

    if intro_flag:
        door_flag = False
        print('Возьми нужные предметы, а затем введи "готов" для продолжения \n')
        anwser = input('Твой выбор(готов или измени набор предметов?): ').lower()
        cleared_anwser = re.split(r'[,:;\s]+', anwser)
        if anwser in finish_anwser and selected_items:  #Если ответ о готовности верный и список предметов не пустой
            print(f'\nОтлично, вы готовы продолжать!\nВаш инвентарь:\
            -<{', '.join(selected_items)}>-\nИдем дальше!')
            intro_flag = False
            door_flag = True
        elif return_matches(cleared_anwser, items_list):  #Если пересекающееся множество не пустое
            selected_items = return_matches(cleared_anwser, items_list)  #то в переменную записываем список с элементами пересекающихся множеств
            print(f'Вы выбрали: -<{', '.join(selected_items)}>-\n')
        else:
            print('Либо ты ничего не выбрал, либо нет такого предмета!\
                   Сделай выбор\n')
            print(f'Ты ввел: {anwser}')
    
    if door_flag:
        print('Перед Вами дверь\n')
        
        try:
            key_for_door = selected_items.index('ключ')   #проверка наличия 'ключа' по индексу в списке ранее выбранного инвентаря
            try:              
                door_key = input('Что используете, чтобы открыть дверь?: \n').lower()
                if door_key == 'ключ':
                    print('Дверь открылась! Вы вышли в коридор.\n')
                    door_flag = False
                    wizard_flag = True
                    
                elif door_key not in selected_items:
                    print(f'Ошибка: Такого предмета нет\nНапоминаю, в вашем инвентаре: -<{', '.join(selected_items)}>-\n')
                else:
                    # door_flag = True
                    raise ValueError('Ошибка: Этот предмет не подходит!\n')
         
            except ValueError as e:                
                print(e)
        except ValueError:
            intro_flag = True
            print('В вашем инвентаре нет ключа для двери. Измените инвентарь\n')
    
    if wizard_flag:
        print('Вас встречает маг, который задаёт загадку.\nИгроку даётся 2 попытки.\n''')
        question = ('Что можно держать в правой руке, но нельзя в левой?:\n\
        1) Левую руку\n\
        2) Воздух\n\
        3) Огонь\n')
        print(question)
        try:
            for attempt in range(2, 0, -1):                   
                anwser = input('Ваш ответ (1, 2 или 3): ')
                if anwser == '1':
                    print('Верно! Маг пропускает вас дальше.\n')
                    print('Вы вышли на мост, который может обрушиться.\n')
                    wizard_flag = False
                    bridge_flag = True
                    break
                else:
                    print('Неверно! Попробуйте ещё раз.\n\
                    Осталось попыток:', attempt - 1)
            else:
                wizard_flag = False
                game_flag = False
                raise Exception('Маг исчез в тени...')
        except Exception as e:
            print(e)

    while bridge_flag:
        print('У вас есть 3 варианта:\n\
        1) Прыгнуть – безопасно.\n\
        2) Бежать вперёд – 50% шанс спастись.\n\
        3) Остаться на месте – мост ломается, игрок проигрывает\n')
        anwser = input('Ваш выбор (1, 2 или 3): \n')
        try:
            if anwser_func(anwser) == '1':
                print("Ты справился! Впереди тебя ждет финальное испытание")
                print('Игрок добирается до финальных ворот, но их нужно взломать.\n')
                bridge_flag = False
                final_flag = True
                break
            
            elif anwser_func(anwser) == '3':
                raise Exception('\nОшибка: Пол обрушился, и вы упали в пропасть!\n')
            else:
                print('Неверный ответ. Выбери один из 3х вариантов')
        except Exception as e:
            print(e)

    if final_flag:
        print('Взлом состоит из цикла: игрок 3 раза вводит код.\n\
        • Если код "777" – ворота открываются.\n\
        • Если после 3 попыток код неверный – игрок попадает в ловушку\n')
        attempts_count = 0
        try:
            while attempts_count < 3:
                attempts_count += 1
                anwser = input('Введи код: ')
                if anwser == '777':
                    print('Ворота открылись! Вы выбрались из замка!\nПозравляю с победой!')
                    final_flag = False
                    game_flag = False
                    break
                else:
                    print('Неверно!')
            else:
                raise Exception('Вы попали в ловушку и скоропостижно скончались\nИгра окончена!')
        except Exception as e:
            print(e)
            game_flag = False
         


