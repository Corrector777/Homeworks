from contextlib import contextmanager
import time
import random

# Задача 1: Контекстный таймер для операций

# Создайте функцию-генератор operation_timer() с декоратором @contextmanager ,
# которая:
# 1. Замеряет время в миллисекундах до и после выполнения блока кода
# 2. Возвращает затраченное время как результат работы менеджера
# 3. Может использоваться с оператором with и именованной переменной

# Эти функции уже готовы, их не нужно менять

def password_crack_simulation():
    """Имитирует процесс подбора пароля"""
    time.sleep(random.uniform(0.1, 0.7))
    return "P@ssw0rd123"


def database_query_simulation():
    """Имитирует запрос к базе данных"""
    time.sleep(random.uniform(0.3, 0.7))
    return ["user_data.txt", "admin_credentials.db", "security_logs.csv"]


def server_connection_simulation():
    """Имитирует подключение к серверу"""
    time.sleep(random.uniform(0.1, 0.5))
    return {"status": "connected", "address": "192.168.1.1", "port": 22}


# Ваш код должен начинаться отсюда
class OperationTimer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        self.elapsed_time = (self.end_time - self.start_time) * 1000
    
          
# Примеры использования


print("Миссия 1: Измерение времени операций")
print("-" * 50)

with OperationTimer() as timer:
    password = password_crack_simulation()
print(f"Подбор пароля занял {timer.elapsed_time:.2f} мс. Пароль: {password}")
with OperationTimer() as timer:
    files = database_query_simulation()
print(f"Запрос к базе данных занял {timer.elapsed_time:.2f} мс. Найдено файлов: {len(files)}")
with OperationTimer() as timer:
    connection = server_connection_simulation()
print(f"Подключение к серверу заняло {timer.elapsed_time:.2f} мс. Статус: {connection['status']}")


# Ожидаемый вывод (значения времени будут отличаться):
# Миссия 1: Измерение времени операций
# --------------------------------------------------
# Подбор пароля занял 234.56 мс. Пароль: P@ssw0rd123
# Запрос к базе данных занял 456.78 мс. Найдено файлов: 3
# Подключение к серверу заняло 678.90 мс. Статус: connected