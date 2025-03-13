import random
# Задание 1: Декоратор для логирования

# def log_auth(func):  # Декоратор
#     def wrapper(*args, **kwargs):  # обертка  функции authenticate
#         print(f'Функция {func.__name__} вызвана с аргументами {args}')
#         print(func(*args))   
#     return wrapper


# @log_auth   # применяем декоратор
# def authenticate(user=None, password=None):
#     '''функция идентификации пользователя.
#     ARGS: имя пользователя, пароль
#     Возвращает: True, если пароль = password123, иначе - False'''
#     if password == 'password123':
#         return True
#     return False
    

# authenticate('Иван', 'password123')
# authenticate('Иван', 'password1')


# Задание 2: Декоратор для проверки прав доступа
# access_list = ['admin', 'manager']  # список доступных ролей


# def check_permission(access_list):  параметризированный декоратор(принимает список ролей)
#     def decorator(func):  декоратор
#         def wrapper(username, role):  обертка функции сheck_permission
#             if role in access_list:  проверка.если аргумент в разрешенном списке
#                 result = func(username, role)  вызываем функцию и выводим успешное сообщение
#                 print(result)
#             else:
#                 print('У вас нет прав для выполнения этой операции') Если аргумент не в списке, выводим сообщение о запрете и функцию не вызываем
#         return wrapper
#     return decorator 
        

# @check_permission(access_list)  # применяем параметризированный декоратор
# def delete_user(username, role):
#     return f'Пользователь {username} успешно удален'


# delete_user('user1', 'manager')
# delete_user('user1', 'bob')
# delete_user('user2', 'admin')


# Задание 3: Декоратор для кэширования результатов


# def cache_result(func):  # Декоратор
#     cash_dict = {}  # словарь -кэш в декораторе до вызова обертки
   
#     def wrapper(numbers):  # обертка, которая осуществит вызов функции calculate_average
#         if tuple(numbers) in cash_dict:  # проверяем наличие ключа в словаре
#             print(f'{cash_dict[tuple(numbers)]} (из кэша)') # если ключ найден в слове,берем значение из словаря
#         else:
#             cash_dict[tuple(numbers)] = func(numbers)  # если ключ не найден, создаем ключ-значение и обновляем словарь
#             result = func(numbers)  # вызываем функцию и присваиваем результат ее вызова переменной result
#             print(result)  # выводим значение из вызванной функции
#     return wrapper  # декоратор возвращает саму функцию wrapper, которая по сути заменяет функцию calculate_average при вызове последней


# @cache_result   # применяем декоратор
# def calculate_average(numbers_list):
    # '''Функция подсчета среднего арифметического всех чисел в списке
    # Аргументы: список чисел
    # возвращает среднее арифметическое'''
#     count = 0
#     sum_of_numbers = 0
#     for i in numbers_list:
#         count += 1
#         sum_of_numbers += i
#     averange = sum_of_numbers / count 
#     return averange


# calculate_average([1, 2, 3])
# calculate_average([1, 2, 3])
# calculate_average([1, 2, 3])
# calculate_average([1, 5, 3])
# calculate_average([1, 5, 3])

# Задание 4: Декоратор для повторного выполнения при ошибке
retries = 3  # кол-во попыток

def retry_on_failure(retries=3):  # декоратор параметризованный.Аргумент- кол-во попыток
    def decorator(func):  # декоратор функции
        def wrapper(message):  # обертка
            for attemp in range(retries):  # задаем цикл с количеством итераций = кол-ву попыток
                try:   # в блоке try-except  отлавливаем вброшенную ошибку
                    result = func(message) # переменной присваиваем значение вызова функции Trur or not
                    if result:  # если True
                        print(f"Уведомление отправлено : {message}")  # уведомляем, что отправлено сообщение
                        return True   # возвращаем True, на этом функция wrapper свою работу завершает
                except ValueError:  # если ловим ошибку, выдаем сообщение о неудаче и продолжаем цикл
                    print(f'Попытка {attemp + 1} не удалась. Сообщение не отправлено')           
            print(f'Не удалось выполнить операцию после {retries} попыток')  # если за время цикла удачной попытки не случилось, то выводим итоговое сообщение       
        return wrapper  # возвращаем wrapper
    return decorator  # возвращаем decorator


@retry_on_failure(retries)  # применяем декоратор
def send_notification(message): 
    '''функция отправки сообщения
       Принимает  сообщение(строку)
       либо выдает ошибку,либо разрешает отпавку'''
    if random.choice([True, False]):
        raise ValueError('Ошибка! Отправка не вышла')
    else:
        return True    



send_notification('Привет, пользователь')


