import logging
from logging.handlers import TimedRotatingFileHandler
import time
from datetime import datetime

## **Задание 2. “Ночной дежурный”**

# **ТЗ:**
# 1. Логгер fleet.archive, уровень WARNING. 
# 2. Файл = combat.log.   
# 3. Ротация: каждый день в полночь.
# 4. Хранить 7 архивов. 
# 5. Формат: %(asctime)s | %(levelname)s | %(message)s. 
# 6. Симуляция: одна запись в секунду в течение 10 с.
    
# Логгер ночного дежурного
logger = logging.getLogger('fleet.archive')
# TODO: установить уровень логирования WARNING
logger.setLevel(logging.WARNING)
# TODO: создать TimedRotatingFileHandler:
#   - filename = 'combat.log'
#   - when = 'midnight', interval = 1
#   - backupCount = 7
handler = TimedRotatingFileHandler(
    'combat.log',
    when='midnight',
    interval=1,
    backupCount=7
    # …
)
# TODO: создать форматтер "%(asctime)s | %(levelname)s | %(message)s"
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
# TODO: установить форматтер    
handler.setFormatter(formatter)

# TODO: добавить handler к logger
logger.addHandler(handler)

# --- Симуляция: боевые события каждую секунду 10 секунд ---
start = datetime.now()
while (datetime.now() - start).seconds < 10:
    # TODO: вызвать logger.warning или logger.error с текстом события
    logger.warning("Simulate some combat event")
    print(f"{datetime.now()}: Simulate nightly combat event")
    time.sleep(1)
