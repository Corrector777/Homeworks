from contextlib import contextmanager
import os
import random
import time

# Эти функции уже готовы, их не нужно менять
def create_config_file(filename, config_type, entries=5):
    """Создает тестовый конфигурационный файл заданного типа"""
    config_templates = {
    "server": [
    "hostname: server{}.example.com",
    "ip_address: 10.0.{}.{}",
    "port: {}",
    "max_connections: {}",
    "timeout: {}"
    ],
    "security": [
    "firewall: {}",
    "encryption: {}",
    "auth_method: {}",
    "max_attempts: {}",
    "lockout_time: {}"
    ],
    "database": [
    "db_name: {}",
    "db_user: user{}",
    "db_port: {}",
    "max_queries: {}",
    "backup_time: {}:00"
    ]
        }
    templates = config_templates.get(config_type, config_templates["server"])
    with open(filename, 'w') as f:
        f.write(f"# {config_type.upper()} CONFIGURATION\n")
        f.write(f"# Generated for testing purposes\n")
        for i in range(entries):
            template = random.choice(templates)
            if "{}" in template:
                if "hostname" in template:
                    value = template.format(random.randint(1, 10))
                elif "ip_address" in template:
                    value = template.format(random.randint(0, 255), random.randint(0, 255))
                elif "port" in template or "db_port" in template:
                    value = template.format(random.choice([80, 443, 3306, 5432, 27017]))
                elif "firewall" in template:
                    value = template.format(random.choice(["enabled", "disabled"]))
                elif "encryption" in template:
                    value = template.format(random.choice(["AES256", "RSA2048", "None"]))
                elif "auth_method" in template:
                    value = template.format(random.choice(["password", "key", "cert", "2FA"]))
                elif "db_name" in template:
                    value = template.format(random.choice(["users", "products", "logs", "metrics"]))
                elif "db_user" in template:
                    value = template.format(random.randint(1, 5))
                elif "backup_time" in template:
                    value = template.format(random.randint(0, 23))
                else:
                    value = template.format(random.randint(10, 100))
            else:
                value = template
            f.write(value + "\n")
    print(f"Создан тестовый конфиг: {filename}")



def cleanup_config_files(*filenames):
    """Удаляет указанные конфигурационные файлы"""
    for filename in filenames:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Удален конфиг: {filename}")


# Ваш код должен начинаться отсюда
@contextmanager
def multi_file_reader(filenames):
    print(f'\nОткрываю множественное чтение из {len(filenames)} файлов...')
    try:
        all_files_lines = []
        statistics = {}
        for filename in filenames:
            with open(filename, 'r') as f:
                lines = f.read().strip().split('\n')
                statistics[filename] = len(lines)
                for line in lines:
                    if line.startswith('#'):
                        continue
                    else:
                        line = f'[{filename}] {line}'
                        all_files_lines.append(line)                
        yield all_files_lines
    except Exception as e:
        print(f'Произошла ошибка: {e}')
    finally:
        print('\nСтатистика чтения:')
        for k, v in statistics.items():
            print(f'- {k}: прочитано {v} строк')
        print(f'\nЗакрываю множественное чтение из {len(filenames)} файлов...\n')
        

# Пример использования
print("\nЗадание 3: Обработка нескольких конфигурационных файлов")
print("-" * 50)
# Создаем тестовые конфигурационные файлы
config_files = [
("server_config.txt", "server"),
("security_config.txt", "security"),
("database_config.txt", "database")
]
# Удаляем файлы, если они уже существуют
for filename, _ in config_files:
    if os.path.exists(filename):
        os.remove(filename)

# Создаем тестовые конфигурационные файлы
for filename, config_type in config_files:
    create_config_file(filename, config_type, random.randint(5, 10))

try:
    # Ищем интересующие нас конфигурации
    search_terms = ["firewall", "password", "encryption", "port", "user"]
    found_configs = []
    print(f"\nПоиск конфигураций, связанных с: {', '.join(search_terms)}")
    # Используем контекстный менеджер для работы с несколькими файлами
    with multi_file_reader([f[0] for f in config_files]) as lines:
        for line in lines:
            # Пропускаем комментарии
            if line.startswith('#'):
                continue
        # Проверяем, содержит ли строка искомые термины
            if any(term in line.lower() for term in search_terms):
                found_configs.append(line)
        # Выводим результаты
        print(f"\nНайдено {len(found_configs)} интересных конфигураций:")
        for config in found_configs:
            print(f" {config}")
except Exception as e:
    print(f"Произошла ошибка при обработке файлов: {e}")
finally:
# Удаляем тестовые файлы
    cleanup_config_files(*[f[0] for f in config_files])


# Ожидаемый вывод:
# Задание 3: Обработка нескольких конфигурационных файлов
# --------------------------------------------------
# Создан тестовый конфиг: server_config.txt
# Создан тестовый конфиг: security_config.txt
# Создан тестовый конфиг: database_config.txt
#
# Поиск конфигураций, связанных с: firewall, password, encryption, port, user
# Открываю множественное чтение из 3 файлов...
#
# Найдено 7 интересных конфигураций:
# [server_config.txt:4] port: 443
# [security_config.txt:2] firewall: enabled
# [security_config.txt:3] encryption: AES256
# [security_config.txt:4] auth_method: password
# [database_config.txt:3] db_user: user3
# [database_config.txt:4] db_port: 3306
# [database_config.txt:6] db_user: user1
#
# Статистика чтения:
# - server_config.txt: прочитано 7 строк
# - security_config.txt: прочитано 7 строк
# - database_config.txt: прочитано 7 строк
# Закрываю все файлы...
# Удален конфиг: server_config.txt
# Удален конфиг: security_config.txt
# Удален конфиг: database_config.txt