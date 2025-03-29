from contextlib import contextmanager
import os
import random


# Эти функции уже готовы, их не нужно менять
def create_server_log(filename, entries=10):
    """Создает тестовый файл лога сервера"""
    ip_addresses = ["192.168.1." + str(i) for i in range(1, 20)]
    actions = ["LOGIN", "LOGOUT", "DOWNLOAD", "UPLOAD", "DELETE", "CREATE"]
    statuses = ["SUCCESS", "FAILED", "ERROR", "DENIED"]
    with open(filename, 'w') as f:
        for _ in range(entries):
            ip = random.choice(ip_addresses)
            timestamp = f"2023-03-{random.randint(1, 30):02d} {random.randint(0, 23):02d}:{random.randint(0, 59):02d}"
            action = random.choice(actions)
            status = random.choice(statuses)
            user = f"user{random.randint(1, 5)}"
            f.write(f"{timestamp} | {ip} | {user} | {action} | {status}\n")
    print(f"Создан тестовый лог: {filename}")



def analyze_log_entry(entry):
    """Анализирует строку лога и возвращает структурированную информацию"""
    parts = entry.strip().split(" | ")
    if len(parts) != 5:
        return None
    timestamp, ip, user, action, status = parts
    return {
        "timestamp": timestamp,
        "ip": ip,
        "user": user,
        "action": action,
        "status": status,
        "suspicious": "TRUE" if status in ["FAILED", "ERROR", "DENIED"] else
        "FALSE"
        }


def cleanup_files(*filenames):
    """Удаляет указанные файлы, если они существуют"""
    for filename in filenames:
        if os.path.exists(filename):
            os.remove(filename)
        print(f"Файл удален: {filename}")


# Ваш код должен начинаться отсюда
@contextmanager
def file_pair(input_file, output_file):
# Напишите ваш код здесь
    print(f"Открываю пару файлов: {input_file}(чтение) и {output_file}(запись)")
    try:
        with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
            yield in_file, out_file   
    finally:
        print(f"Закрываю пару файлов: {input_file} и {output_file}") 

# Пример использования

print("Задание 1: Обработка серверных логов")
print("-" * 50)
# Создаем тестовый лог
log_file = "server.log"
report_file = "suspicious_activity.csv"
# Удаляем файлы, если они уже существуют
cleanup_files(log_file, report_file)
# Создаем тестовый лог
create_server_log(log_file, 15)
try:
    # Используем контекстный менеджер для обработки файлов
    with file_pair(log_file, report_file) as (log, report):
        # Записываем заголовок CSV
        report.write("timestamp,ip,user,action,status,suspicious\n")
        # Обрабатываем каждую строку лога
        suspicious_count = 0
        total_entries = 0
        for line in log:
            total_entries += 1
            entry_data = analyze_log_entry(line)
            if entry_data:
                # Записываем данные в CSV
                csv_line = ",".join([
                entry_data["timestamp"],
                entry_data["ip"],
                entry_data["user"],
                entry_data["action"],
                entry_data["status"],
                entry_data["suspicious"]
                ])
                report.write(csv_line + "\n")
            # Считаем подозрительные записи
            if entry_data["suspicious"] == "TRUE":
                suspicious_count += 1
        # Выводим результаты
        print(f"Обработка завершена: проанализировано {total_entries} записей, найдено {suspicious_count} подозрительных")
# Показываем начало отчета
    print("\nНачало отчета о подозрительной активности:")
    with open(report_file, 'r') as f:
        for i, line in enumerate(f):
            if i < 5: # Показываем только первые 5 строк
                print(line.strip())
            else:
                print("...")
                break
except Exception as e:
    print(f"Произошла ошибка при обработке файлов: {e}")
finally:
# В конце удаляем тестовые файлы
    cleanup_files(log_file, report_file)


# Ожидаемый вывод:
# Задание 1: Обработка серверных логов
# --------------------------------------------------
# Создан тестовый лог: server.log
# Открываю пару файлов: server.log (чтение) и suspicious_activity.csv (запись)
# Обработка завершена: проанализировано 15 записей, найдено 6 подозрительных
# Закрываю файлы: server.log и suspicious_activity.csv
#
# Начало отчета о подозрительной активности:
# timestamp,ip,user,action,status,suspicious
# 2023-03-15 10:25,192.168.1.5,user3,DOWNLOAD,SUCCESS,FALSE
# 2023-03-08 17:42,192.168.1.12,user1,DELETE,FAILED,TRUE
# 2023-03-22 09:18,192.168.1.3,user4,LOGIN,SUCCESS,FALSE
# ...
# Файл удален: server.log
# Файл удален: suspicious_activity.csv