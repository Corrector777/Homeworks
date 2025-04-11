import time
import random
import logging


# 1. Используй стандартный модуль logging .
# 2. Настрой базовую конфигурацию с помощью logging.basicConfig :
# Уровень логирования: logging.DEBUG (чтобы видеть все детали во время этой
# "диагностики").
# Формат лога: Включи время ( asctime ), уровень ( levelname ) и само сообщение
# ( message ). Используй формат времени %Y-%m-%d %H:%M:%S .
# 3. В приложенном скрипте system_check.py добавь логирование:
# DEBUG: Логируй начало и конец каждой функции проверки ( check_processor ,
# check_memory , check_network_link ). Можешь добавить и внутренние шаги, если
# хочешь (например, "Проверяем температуру ядра...").
# INFO: Логируй результат каждой проверки (например, "Процессор: OK", "Память:
# Загружено 75%", "Сетевое соединение: Установлено").
# INFO: Логируй общее начало и конец всего скрипта диагностики.

# system_check.py
# --- НАЧАЛО НАСТРОЙКИ ЛОГИРОВАНИЯ ---
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")
# --- КОНЕЦ НАСТРОЙКИ ЛОГИРОВАНИЯ ---


def check_processor():
    logging.debug("Начало проверки процессора...")
    time.sleep(random.uniform(0.1, 0.5)) # Имитация проверки
    load = random.randint(10, 90)
    logging.debug(f"Процессор загружен на: {load}%")
    temperature = random.randint(40, 85)
    logging.debug(f"Проверяем температуру ядра...")
    result = "OK" if temperature < 80 else "WARNING: High Temperature"
    logging.debug("Проверка процессора завершена.")
    return result


def check_memory():
    logging.debug("Начало проверки памяти...")
    time.sleep(random.uniform(0.1, 0.3))  # Имитация проверки
    total_mem = 16384  # MB
    used_mem = random.randint(4096, 14000)
    logging.debug(f"Использовано {used_mem} MB памяти из {total_mem} MB")
    usage_percent = round((used_mem / total_mem) * 100)
    result = f"Загружено {usage_percent}%"
    logging.debug("Проверка памяти завершена.")
    return result


def check_network_link():
    logging.debug("Начало проверки сетевого соединения...")
    time.sleep(random.uniform(0.2, 0.6)) # Имитация проверки
    logging.debug("Устанавливаем соединение...")
    connection_status = random.choice(["Установлено", "Ошибка: Таймаут", "Нет подключения"])
    if connection_status == "Установлено":
        latency = random.randint(5, 50)
        logging.debug("Соединение устанавливается...")
        time.sleep(latency / 10)
    else:
        logging.warning("Соединение не установлено!")    
    logging.debug("Проверка сетевого соединения завершена.")
    return connection_status


def run_diagnostics():
    print("--- System Diagnostics ---")
    
    proc_status = check_processor()
    logging.info(f"Процессор: {proc_status}")
    mem_status = check_memory()
    logging.info(f"Память: {mem_status}")       
    net_status = check_network_link()
    logging.info(f"Сетевое соединение: {net_status}")
    print("-------------------------")


if __name__ == "__main__":
    logging.info("Начало диагностики")
    run_diagnostics()
    logging.info("Диагностика завершена")