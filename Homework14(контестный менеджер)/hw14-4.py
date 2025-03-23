from contextlib import contextmanager
import random
import time

# Задача 4: Имитация и мониторинг подключений
# Техническое задание
# Создайте функцию-генератор secure_connection() с декоратором @contextmanager, которая:
# 1. Принимает хост и учетные данные для подключения
# 2. Имитирует установку соединения и возвращает объект соединения
# 3. Обрабатывает возможные ошибки при работе с соединением
# 4. Всегда корректно закрывает соединение, даже при возникновении ошибок
# 5. Логирует все этапы работы с соединением

# Эти классы и функции уже готовы, их не нужно менять
class ConnectionError(Exception):
    """Ошибка подключения к серверу"""
    pass

class AuthenticationError(Exception):
    """Ошибка аутентификации"""
    pass

class PermissionError(Exception):
    """Ошибка доступа"""
    pass


def simulate_connection_attempt(host, credentials):
    """Имитирует попытку подключения к серверу"""
    print(f"Попытка подключения к {host} с учетными данными {credentials}...")
    time.sleep(random.uniform(0.5, 1.0))
    # Симуляция различных проблем подключения
    if "firewall" in host:
        if random.random() < 0.7: # 70% шанс ошибки для firewall серверов
            raise ConnectionError(f"Не удалось подключиться к {host}: блокировка брандмауэра")
    if credentials == "guest:1234":
        if random.random() < 0.5: # 50% шанс ошибки для гостевых учетных данных
            raise AuthenticationError("Неверные учетные данные")
    # Успешное подключение
    connection = {
    "host": host,
    "status": "connected",
    "session_id": random.randint(10000, 99999),
    "encrypted": True
    }
    return connection


# Ваш код должен начинаться отсюда
@contextmanager
def secure_connection(host, credentials):
    print(f"[ПОДКЛЮЧЕНИЕ] Устанавливаю соединение с {host}...")
# На здесь
    try:
        simalate_connection = simulate_connection_attempt(host, credentials)
        print(f"[ПОДКЛЮЧЕНИЕ] Соединение с {host} установлено успешно")
        yield simalate_connection   
    except ConnectionError as e:
        print(f"[ОШИБКА] {e}")
        raise ConnectionError(e)
    except AuthenticationError as e:
        print(f"[ОШИБКА] {e}")
        raise AuthenticationError(e)
    except PermissionError as e:
        print(f"[ОШИБКА] {e}")
        raise PermissionError(e)    
  
    finally:
        print(f"[ПОДКЛЮЧЕНИЕ] Закрываю соединение с {host}...")    





# Примеры использования
print("\nМиссия 4: Безопасные подключения")
print("-" * 50)
# Успешное подключение
print("\nПопытка 1: Стандартный сервер с правильными учетными данными")
try:
    with secure_connection("database.techsafe.com", "admin:secure123") as conn:
        print(f"Соединение установлено! ID сессии: {conn['session_id']}")
        print(f"Выполнение операций с {conn['host']}...")
        time.sleep(0.5) # Имитация работы
except Exception as e:
    print(f"Произошла необработанная ошибка: {e}")

# Подключение с ошибкой брандмауэра
print("\nПопытка 2: Сервер с брандмауэром")
try:
    with secure_connection("firewall.techsafe.com", "admin:secure123") as conn:
        print(f"Соединение установлено! ID сессии: {conn['session_id']}")
        print(f"Выполнение операций с {conn['host']}...")
        time.sleep(0.5) # Имитация работы
except ConnectionError as e:
    print(f"Ошибка подключения обработана: {e}")


# # Подключение с ошибкой аутентификации
print("\nПопытка 3: Использование гостевых учетных данных")
try:
    with secure_connection("backup.techsafe.com", "guest:1234") as conn:
        print(f"Соединение установлено! ID сессии: {conn['session_id']}")
        print(f"Выполнение операций с {conn['host']}...")
        time.sleep(0.5) # Имитация работы
except AuthenticationError as e:
    print(f"Ошибка аутентификации обработана: {e}")


# # Подключение с последующей ошибкой при выполнении операций
print("\nПопытка 4: Успешное подключение, но ошибка в операциях")
try:
    with secure_connection("admin.techsafe.com", "admin:secure123") as conn:
        print(f"Соединение установлено! ID сессии: {conn['session_id']}")
        print(f"Выполнение операций с {conn['host']}...")
        time.sleep(0.5) # Имитация работы
        if "admin" in conn['host']:
            raise PermissionError("Недостаточно прав для выполнения операции")
except PermissionError as e:
    print(f"Ошибка доступа обработана: {e}")

# Ожидаемый вывод (будет отличаться из-за случайных факторов):
# Миссия 4: Безопасные подключения
# --------------------------------------------------
#
# Попытка 1: Стандартный сервер с правильными учетными данными безопасно и эффективно."
# [ПОДКЛЮЧЕНИЕ] Устанавливаю соединение с database.techsafe.com...
# Попытка подключения к database.techsafe.com с учетными данными admin:secure123...
# [ПОДКЛЮЧЕНИЕ] Соединение установлено успешно
# Соединение установлено! ID сессии: 54321
# Выполнение операций с database.techsafe.com...
# [ПОДКЛЮЧЕНИЕ] Закрываю соединение с database.techsafe.com...
#
# Попытка 2: Сервер с брандмауэром
# [ПОДКЛЮЧЕНИЕ] Устанавливаю соединение с firewall.techsafe.com...
# Попытка подключения к firewall.techsafe.com с учетными данными admin:secure123...
# [ОШИБКА] Не удалось подключиться к firewall.techsafe.com: блокировка брандмауэра
# Ошибка подключения обработана: Не удалось подключиться    