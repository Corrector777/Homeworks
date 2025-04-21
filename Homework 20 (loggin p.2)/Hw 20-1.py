import logging
from logging.handlers import RotatingFileHandler
import time
import os

## **Задание 1. “Первая смена архива”**

# **Сюжет:**

# Архивариус Звёздного Флота получил от инженерного отдела USS “Энтерпрайз” стенограммы показаний датчиков. Файл растёт быстро, и наша задача – настроить ротацию так, чтобы при достижении 1 MB «сменялся» новый архив, а на борту хранились только два предыдущих файла.

# **ТЗ:**

# 1. Логгер fleet.archive, уровень INFO.
# 2. Пишем в engineering.log.
# 3. Ротация по размеру = 1 MB
# 4. Хранить 2 архива.
# 5. Формат: %(asctime)s | %(levelname)s | %(message)s.
# 6. Симуляция: 100 сообщений с паузой.


# Инициализируем логгер Архивариуса
logger = logging.getLogger('fleet.archive')
# TODO: установить уровень логирования INFO
logger.setLevel(logging.INFO)

# TODO: создать RotatingFileHandler:
#   - путь = 'engineering.log'
#   - maxBytes = 1*1024*1024
#   - backupCount = 2
handler = RotatingFileHandler(
    'engineering.log',
    maxBytes=1*1024*1024,
    backupCount=2
)
# TODO: создать форматтер "%(asctime)s | %(levelname)s | %(message)s"
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
handler.setFormatter(formatter)

# TODO: прикрепить handler к logger
logger.addHandler(handler)
# --- Симуляция: генерируем 100 инженерных сообщений ---
for i in range(100):
    # TODO: вызвать logger.info с текстом вроде "Sensor reading #{i}"
    logger.info(f"Sensor reading #{i}")
    print(f"Simulate log message #{i}")
    time.sleep(0.05)


