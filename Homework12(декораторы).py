# Задание 1: Декоратор для логирования

def log_auth(func):
    def wrapper(*args, **kwargs):    
        print(f'Функция {func.__name__} вызвана с аргументами {args}')
        print(func(*args))   
    return wrapper


@log_auth
def authenticate(user=None, password=None):
    '''функция идентификации пользователя.
    ARGS: имя пользователя, пароль
    Возвращает: True, если пароль = password123, иначе - False'''
    if password == 'password123':
        return True
    return False
    

authenticate('Иван', 'password123')
authenticate('Иван', 'password1')


# Задание 2: Декоратор для проверки прав доступа

