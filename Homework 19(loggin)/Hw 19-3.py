import logging
import sys
import time
import random
from pythonjsonlogger import jsonlogger


# ТЗ:
# 1. Установи библиотеку: pip install python-json-logger .
# 2. Настрой логирование так, чтобы оно выводило сообщения в формате JSON.
# Используй pythonjsonlogger.jsonlogger.JsonFormatter .
# 3. Настрой StreamHandler для вывода логов в консоль ( sys.stdout ).
# 4. В формате лога должны присутствовать как минимум timestamp , level
# (переименованный из levelname ), name (имя логгера) и message .
# 5. В приложенном скрипте analyze_comms.py добавь логирование:
# Получи именованный логгер, например: logger =
# logging.getLogger('valentinos_traffic_analyzer') .
# Для каждой "транзакции" (словарь в traffic_data ) логируй сообщение уровня
# INFO вида "Обработана транзакция X".
# Ключевое: Используй параметр extra={...} в вызове logger.info() , чтобы
# добавить все поля из словаря транзакции ( transaction_id , sender , receiver ,
# amount , currency , item и т.д.) в JSON-лог как отдельные поля.
# Приложение для логирования ( analyze_comms.py ):
# Если транзакция имеет некорректный тип ( type != 'transfer' ), залогируй
# WARNING с сообщением "Неизвестный тип транзакции" и добавь детали
# транзакции через extra


# --- НАСТРОЙКА JSON ЛОГИРОВАНИЯ ---
# TODO: Получи логгер 'valentinos_traffic_analyzer'
logger = logging.getLogger('valentinos_traffic_analyzer')
logger.setLevel(logging.INFO)
# TODO: Создай StreamHandler для вывода в stdout
handler = logging.StreamHandler(sys.stdout)
# TODO: Создай JsonFormatter (включи 'timestamp', 'level', 'name', 'message', переименуй levelname->level)
formatter = jsonlogger.JsonFormatter(
    '%(timestamp)s %(levelname)s %(name)s %(message)s',
    rename_fields={'levelname': 'level', 'asctime': 'timestamp'},
    datefmt='%Y-%m-%dT%H:%M:%S.%fZ',
    json_ensure_ascii=False
)
# TODO: Установи форматтер для хэндлера
handler.setFormatter(formatter)
# TODO: Добавь хэндлер к логгеру (с проверкой, чтобы не дублировать)
if not logger.handlers:
    logger.addHandler(handler)
# --- КОНЕЦ НАСТРОЙКИ ЛОГИРОВАНИЯ ---


# Имитация перехваченного трафика Валентино
traffic_data = [
    {'transaction_id': 'txn_v_001', 'type': 'transfer', 'sender':
        'jackie_w', 'receiver': 'gustavo_o', 'amount': 1500, 'currency': 'E$',
        'timestamp': '2077-10-26T14:30:15Z'},
    {'transaction_id': 'txn_v_002', 'type': 'transfer', 'sender': 'padre_j',
        'receiver': 'el_coyote_c', 'amount': 500, 'currency': 'E$', 'item_code':
        'DRUGS_GLITTER', 'timestamp': '2077-10-26T14:32:01Z'},
    {'transaction_id': 'txn_v_003', 'type': 'ping', 'sender': 'unknown',
        'receiver': 'broadcast', 'timestamp': '2077-10-26T14:33:00Z'}, # Неизвестный тип
    {'transaction_id': 'txn_v_004', 'type': 'transfer', 'sender':
        'valeria_h', 'receiver': 'marco_r', 'amount': 850, 'currency': 'E$',
        'timestamp': '2077-10-26T14:35:22Z'},
# Добавь больше примеров, если хочешь
]


def process_transaction(transaction):
    tx_id = transaction.get('transaction_id', 'unknown')
    tx_type = transaction.get('type')
    if tx_type == 'transfer':
        # TODO: Залогируй INFO "Обработана транзакция" и передай ВСЕ поля транзакции в 'extra'
        log_extra = transaction.copy() # Копируем, чтобы не модифицировать оригинал, если нужно
        logger.info(f"Обработана транзакция {tx_id}", extra=log_extra)  # Передаем в extra все поля транзакции (transaction)
        # Имитация какой-то полезной работы
        time.sleep(random.uniform(0.05, 0.15))
        return True
    else:
        # TODO: Залогируй WARNING "Неизвестный тип транзакции" и передай ВСЕ поля транзакции в 'extra'
        log_extra = transaction.copy()
        logger.warning(f"Неизвестный тип транзакции {tx_id}", extra=log_extra)
        return False
    

if __name__ == "__main__":
    processed_count = 0
    warning_count = 0
    for tx in traffic_data:
        if process_transaction(tx):
            processed_count += 1
        else:
            warning_count += 1
    print('-------' * 7)
    print(f"Обработано {processed_count} транзакций, {warning_count} предупреждений")