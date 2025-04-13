from loguru import logger # <- Импортируй
import sys
import random
import time
import uuid

# 1. Установи библиотеку: pip install loguru .
# 2. Настрой loguru так, чтобы он писал логи в JSON формате в стандартный вывод
# ( sys.stdout ).
# Удали стандартный обработчик loguru , если он есть ( logger.remove() ).
# Добавь новый обработчик с помощью logger.add(sys.stdout, serialize=True,
# level="INFO") .
# 3. В приложенном скрипте arasaka_connect.py используй loguru :
# При инициации нового соединения генерируй уникальный session_id .
# Используй logger.bind(session_id=session_id) чтобы создать контекстный
# логгер для этой сессии.
# Все последующие логи, связанные с этой сессией (отправка пакета, получение
# ответа, ошибка), делай через этот контекстный логгер
# ( bound_logger.info(...) , bound_logger.error(...) и т.д.). Поле session_id
# будет автоматически добавлено в JSON.
# Логируй следующие события (используя контекстный логгер):
# INFO: Начало установки соединения ( "Initiating connection..." ).
# INFO: Успешное соединение ( "Connection established" ).
# Приложение для логирования ( arasaka_connect.py ):
# DEBUG: Отправка пакета данных ( "Sending data packet" , можно добавить
# размер пакета size=... ). (Установи уровень DEBUG , если хочешь видеть
# это).
# INFO: Получение подтверждения ( "ACK received" , можно добавить номер
# пакета packet_no=... ).
# ERROR: Ошибка соединения или передачи данных ( "Connection error" ,
# "Data transmission failed" ). loguru автоматически добавит traceback,
# если вызван внутри except блока.
# INFO: Завершение соединения ( "Closing connection" ).

# arasaka_connect.py

# --- НАСТРОЙКА LOGURU ДЛЯ JSON ---
# TODO: Удали стандартный хэндлер loguru
logger.remove()
# TODO: Добавь новый хэндлер для вывода JSON в stdout с уровнем INFO
logger.add(
    sys.stdout,
    serialize=True,  # Включаем JSON
    level="DEBUG"  # Устанавливаем минимальный уровень
)
# --- КОНЕЦ НАСТРОЙКИ ЛОГИРОВАНИЯ ---

ARASAKA_SERVER = "arasaka.corp.global"


def generate_session_id():
    return f"session_{uuid.uuid4().hex[:8]}"  # Генерируем уникальный session_id


def send_data_packet(bound_logger, packet_no, data_size):
    # TODO: Используй bound_logger для логирования отправки пакета (DEBUG)
    bound_logger.debug(f"Sending data packet {packet_no} with size {data_size}")
    time.sleep(random.uniform(0.05, 0.2))
    # Имитация возможной ошибки передачи
    if random.random() < 0.1:  # 10% шанс ошибки
        raise ConnectionError(f"Transmission failed for packet {packet_no}")
    # TODO: Используй bound_logger для логирования получения ACK (INFO)
    bound_logger.info(f"Received ACK for packet {packet_no} with size {data_size}")


def connect_and_transfer(server_address):
    session_id = generate_session_id()
    # TODO: Создай контекстный логгер с помощью logger.bind()
    bound_logger = logger.bind(session_id=session_id)
    # TODO: Используй bound_logger для логирования начала соединения (INFO)
    bound_logger.info("Initiating connection...")
    time.sleep(random.uniform(0.2, 0.5))
    # Имитация ошибки подключения
    if random.random() < 0.01: # 20% шанс провала подключения
        # TODO: Используй bound_logger для логирования ошибки подключения (ERROR)
        # loguru сам поймает контекст исключения, если оно есть
        try:
            raise TimeoutError("Failed to establish connection: Server timeout")
        except TimeoutError as e:
            bound_logger.exception(e)
        return False
    # TODO: Используй bound_logger для логирования успешного соединения (INFO)
    bound_logger.info("Connection established")
    # Имитация передачи данных
    num_packets = random.randint(3, 7)
    success = True
    for i in range(1, num_packets + 1):
        try:
            data_size = random.randint(1024, 8192)
            send_data_packet(bound_logger, i, data_size)
        except ConnectionError as e:
            # TODO: Используй bound_logger для логирования ошибки передачи (ERROR)
            # loguru поймает исключение внутри except блока
            bound_logger.exception(e)
            success = False
            break  # Прерываем передачу при ошибке
        except Exception as e:
            # TODO: Используй bound_logger для логирования неожиданной ошибки (CRITICAL)
            bound_logger.critical(e)
            success = False
            break
    # TODO: Используй bound_logger для логирования завершения соединения (INFO)
    status = "successfully" if success else "with errors"
    bound_logger.info(f"Connection closed {status}")
    return success


if __name__ == "__main__":
    logger.info(f"Starting data transfer attempts to {ARASAKA_SERVER}...")
    MAX_ATTEMPTS = 3
    for attempt in range(1, MAX_ATTEMPTS + 1):
        logger.info(f"--- Attempt #{attempt} ---") # Этот лог не будет иметь session_id
        result = connect_and_transfer(ARASAKA_SERVER)
        if result:
            logger.info(f"--- Attempt #{attempt} successful ---")
            break  # Выходим, если успешно
        else:
            logger.warning(f"--- Attempt #{attempt} failed ---")
        if attempt < MAX_ATTEMPTS:
            time.sleep(1)  # Пауза перед следующей попыткой
            logger.info("--- Transfer process finished ---")