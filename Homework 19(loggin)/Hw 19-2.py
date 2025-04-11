import random
import logging
import time


# ТЗ:
# 1. Предполагается, что базовая настройка logging (например, basicConfig с уровнем
# INFO или выше) уже есть (можно скопировать из Задания 1, но установить
# level=logging.INFO ).
# 2. В приложенном скрипте decrypt_shard.py добавь логирование для обработки
# потенциальных проблем:
# INFO: Логируй начало обработки шарда и успешное завершение с извлеченными
# Приложение для логирования ( decrypt_shard.py ):
# данными.
# WARNING: Если в данных шарда отсутствует некритичное поле (например,
# optional_notes ), залогируй предупреждение, но продолжай обработку.
# ERROR: Если отсутствует ключевое поле (например, payload или
# encryption_key ), залогируй ошибку. Используй exc_info=True или
# logger.exception() внутри блока except , чтобы записать traceback исключения
# ( KeyError ).
# ERROR: Если происходит другая непредвиденная ошибка при "расшифровке"
# (имитируется ValueError ), залогируй ее также с деталями исключения.


# --- НАСТРОЙКА ЛОГИРОВАНИЯ (можно взять из Задания 1, level=logging.INFO) -
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
# --- КОНЕЦ НАСТРОЙКИ ЛОГИРОВАНИЯ ---
#Имитация разных дата-шардов от Реджины
shards_data = [
{"id": "shard_001", "encryption_key": "key123", "payload": "Secret data here.", "optional_notes": "Handle with care."},
{"id": "shard_002", "encryption_key": "key456", "payload": "Another secret."},
{"id": "shard_003", "encryption_key": "key789"}, # Отсутствует payload
{"id": "shard_004", "payload": "Data without key."}, # Отсутствует ключ
{"id": "shard_005", "encryption_key": "key101", "payload": "Corrupted data", "checksum": "bad"}, # Имитация ошибки при расшифровке
]


def decrypt_and_process(shard_data):
    shard_id = shard_data.get("id", "unknown_shard")
    logging.info(f"Начало обработки шарда: {shard_id}")
    try:
        # Проверяем наличие ключевых полей
        if "payload" not in shard_data:
            # logging.error(f"Oшибка обработки {shard_id}")  # думаю, что тут этот лог излишен. так как логируется внизу
            raise KeyError("Отсутствует обязательное поле 'payload'")
        if "encryption_key" not in shard_data:
            # logging.error(f"Oшибка обработки {shard_id}")  # думаю, что тут этот лог излишен. так как логируется внизу
            raise KeyError("Отсутствует обязательное поле 'encryption_key'")
        # Проверяем наличие необязательного поля
        if "optional_notes" not in shard_data:
            logging.warning(f"В шарде {shard_id} отсутствует необязательное поле 'optional_notes'.")

        # Имитация процесса расшифровки, который может вызвать ошибку
        payload = shard_data['payload']
        key = shard_data['encryption_key']
        logging.debug(f"Используем ключ {key} для расшифровки...")  # Не выведется, так как уровень DEBUG не установлен
        time.sleep(random.uniform(0.1, 0.4))  # Имитация работы
        if shard_data.get("checksum") == "bad":
            # logging.error(f"Oшибка обработки {shard_id}")  # думаю, что тут этот лог излишен. так как логируется внизу
            raise ValueError("Ошибка целостности данных при расшифровке")
        decrypted_data = f"Расшифровано: '{payload}'"
        logging.info(f"Шард {shard_id} успешно обработан. Данные: {decrypted_data}")
        return decrypted_data
    except KeyError as e:
        # Ошибки KeyError уже должны быть залогированы выше, но можно добавить финальный лог здесь, если нужно
        logging.error(f"Критическая ошибка обработки {shard_id}: {e}", exc_info=True)  # Простой лог, т.к. traceback уже есть
        return None
    except ValueError as e:
        # Ошибки ValueError уже должны быть залогированы выше
        logging.error(f"Критическая ошибка обработки {shard_id}: {e}", exc_info=True)  # Простой лог, т.к. traceback уже есть
        return None
    except Exception as e:
        # Ловим любые другие неожиданные ошибки
        logging.critical(f"Непредвиденная критическая ошибка при обработке {shard_id}: {e}", exc_info=True)
        return None


if __name__ == "__main__":
    print("--- Processing Regina's Shards ---")
    for i, shard in enumerate(shards_data):
        print(f"\n--- Обработка шарда {i+1} ---")
        result = decrypt_and_process(shard)
        if result:
            print(f"Результат: {result}")
        else:
            print("Обработка не удалась. Смотри логи.")
    print("\n--- Все шарды обработаны ---")