from contextlib import contextmanager
import os
import tempfile
import random
import string

# Задание 2: Временный шифрованный файл
# Техническое задание
# Создайте функцию-генератор temp_encrypted_file() с декоратором @contextmanager ,
# которая:

# 1. Принимает данные для записи и ключ шифрования
# Заготовка кода и пример
# 2. Создает временный файл и записывает в него зашифрованные данные
# 3. Возвращает имя временного файла для использования
# 4. При выходе из контекста автоматически удаляет временный файл
# 5. Использует простое XOR-шифрование для защиты данных
# Эти функции уже готовы, их не нужно менять
def xor_encrypt_decrypt(data, key):
    """Простое XOR-шифрование/дешифрование"""
    if not data or not key:
        return data
    # Преобразуем в байты, если нужно
    if isinstance(data, str):
        data = data.encode('utf-8')
    if isinstance(key, str):
        key = key.encode('utf-8')
    # Применяем XOR с циклическим ключом
    result = bytearray(len(data))
    for i in range(len(data)):
        result[i] = data[i] ^ key[i % len(key)]
    return bytes(result)


def generate_random_password(length=10):
    """Генерирует случайный пароль указанной длины"""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))


def read_file_content(filename):
    """Читает и возвращает содержимое файла"""
    with open(filename, 'rb') as f:
        return f.read()


# Ваш код должен начинаться отсюда
@contextmanager
def temp_encrypted_file(data, key):
# Напишите ваш код здесь
    try:
        print('Создаем временный зашифрованный файл...')
        with tempfile.NamedTemporaryFile(mode='wb', delete=False) as temp_file:
            temp_file.write(xor_encrypt_decrypt(data, key))
            temp_file.flush()
            yield temp_file.name
            print(f'Удаляем временный файл {temp_file.name}...')
            os.remove(temp_file.name)
    except Exception as e:
        raise e  
  
        
# Пример использования
print("\nЗадание 2: Работа с временными зашифрованными файлами")
print("-" * 50)
# Подготовка данных
secret_data = "Пароли администраторов:\n" + "\n".join([f"admin{i}: {generate_random_password()}" for i in range(1, 6)])
encryption_key = "S3cr3tK3y!"

print(f"Исходные секретные данные:\n{secret_data}\n")
try:
    # Создаем временный зашифрованный файл
    with temp_encrypted_file(secret_data, encryption_key) as temp_file:
        print(f"Временный файл создан: {temp_file}")
        # Проверяем, что файл существует
        if os.path.exists(temp_file):
            print("Проверка: Файл существует на диске")
            # Попробуем прочитать зашифрованное содержимое
            encrypted_content = read_file_content(temp_file)
            print(f"Зашифрованное содержимое (первые 20 байт): {encrypted_content[:20]}")
            # Дешифруем для проверки
            decrypted_content = xor_encrypt_decrypt(encrypted_content, encryption_key)
            if decrypted_content.decode('utf-8') == secret_data:
                print("Проверка дешифрования: Успешно! Данные идентичны")
            else:
                print("Проверка дешифрования: Ошибка! Данные не совпадают")
        else:
            print("Ошибка: Временный файл не был создан")
    # После выхода из контекста
    if os.path.exists(temp_file):
        print("Предупреждение: Временный файл не был удален!")
    else:
        print("Проверка: Временный файл был успешно удален")

except Exception as e:
    print(f"Произошла ошибка: {e}")
# # Ожидаемый вывод:
# # Задание 2: Работа с временными зашифрованными файлами
# # --------------------------------------------------
# # Исходные секретные данные:
# # Пароли администраторов:
# # admin1: p4ssw0rd!X
# # admin2: s3cretABC
# # admin3: qwerty123!
# # admin4: Admin!@#4
# # admin5: 5trongP@ss
# #
# # Создаю временный зашифрованный файл...
# # Временный файл создан: /tmp/encrypted_tmp_12345.dat
# # Проверка: Файл существует на диске
# # Зашифрованное содержимое (первые 20 байт):
# b'\x10\x1e\x02\x1e\x12\x04\x0f\t\n\x1c\x16\x0f\x1e\x07\x0b...'
# # Проверка дешифрования: Успешно! Данные идентичны
# # Удаление временного файла...
# # Проверка: Временный файл был успешно удален
