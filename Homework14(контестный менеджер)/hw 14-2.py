from contextlib import contextmanager
import os
import types

# Задача 2: Безопасная работа с файлами
# Техническое задание
# Создайте функцию-генератор secret_file() с декоратором @contextmanager , которая:

# 1. Принимает имя файла и режим работы ('r' или 'w')
# 2. Открывает файл в указанном режиме
# 3. Добавляет в начало каждой строки при чтении или записи метку "[СЕКРЕТНО]"
# 4. Гарантирует, что файл будет закрыт при любых обстоятельствах
# 5. Выводит сообщения о начале и окончании работы с файлом

def create_test_file(filename, content):
    """Создает тестовый файл с указанным содержимым"""
    with open(filename, 'w') as f:
        f.write(content)
        print(f"Тестовый файл {filename} создан")


def delete_file_if_exists(filename):    
    """Удаляет файл, если он существует"""
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Файл {filename} удален")


def secret_file_generator(file_obj):
    for line in file_obj:
        yield f"[СЕКРЕТНО] {line.strip()}"

@contextmanager
def secret_file(filename, mode):
# Напишите ваш код здесь
    match mode:
        case 'r':
            # Реализация с изменением строк в файле
            print(f'Открываем файл {filename} в режиме чтения')
            with open(filename, 'r') as f:          
                yield secret_file_generator(f)
                        
        case 'w':
            print(f'Открываем файл {filename} в режиме записи')
            with open(filename, 'w') as f:
                # Определяем вложенную функцию, которая будет записывать в 'f'.
                # Она "захватит" переменную 'f' из внешней области видимости (это называется замыканием).
                
                def secret_write(data):
                    line_to_write = str(data).strip()
                    # Не пишем пустые строки или строки только из пробелов
                    if line_to_write:
                        print(f'Перезаписываем строку: {line_to_write} на: [СЕКРЕТНО] {line_to_write}')
                        f.write(f"[СЕКРЕТНО] {data}")
                # Создаем "обертку" - объект с методом write, который на самом деле наше замыкание        
                wrapper = types.SimpleNamespace(write=secret_write) # Используем SimpleNamespace
                yield wrapper

        case _:
            raise ValueError('Недопустимый режим работы')
    print(f'Закрываем файл {filename}')


test_filename = "secure_data.txt"
create_test_file(test_filename, "имя пользователя: admin\nпароль: supersecret")

print("\nЧтение секретного файла:")
try:
    with secret_file(test_filename, 'r') as file_content:
        for line in file_content:
            print(line)

except Exception as e:
    print(f"Ошибка при чтении файла: {e}")


print("\nЗапись в секретный файл:")
output_filename = "hacker_report.txt"
try:
    with secret_file(output_filename, 'w') as sec_file:
        sec_file.write("доступ получен\n")
        sec_file.write("данные скопированы\n")
except Exception as e:
    print(f"Ошибка при записи в файл: {e}")
# Проверяем, что записалось
print("\nПроверка записанного файла:")
with open(output_filename, 'r') as f:
    print(f.read()) 

# Очистка тестовых файлов
delete_file_if_exists(test_filename)
delete_file_if_exists(output_filename)

# # Чтение секретного файла:
# # Открываю файл secure_data.txt для чтения
# # [СЕКРЕТНО] имя пользователя: admin
# # [СЕКРЕТНО] пароль: supersecret
# # Закрываю файл secure_data.txt
# #
# # Запись в секретный файл:
# # Открываю файл hacker_report.txt для записи
# # Закрываю файл hacker_report.txt
# # Проверка записанного файла:
# # [СЕКРЕТНО] доступ получен
# # [СЕКРЕТНО] данные скопированы
# #
# # Файл secure_data.txt удален
# # Файл hacker_report.txt удален