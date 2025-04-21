import gzip, time
import os
import logging
from logging.handlers import RotatingFileHandler


## **Задание 3. “Архив времён”**

# **ТЗ:**
# 1. Логгер fleet.archive, уровень ERROR.   
# 2. Файл = battle.log.
# 3. Ротация при достижении 10 KB, хранить 3 архива.  
# 4. namer(name): вставляет .YYYY-MM-DD_HH-MM-SS перед расширением.
# 5. rotator(source, dest): создаёт gzip-архив dest+'.gz', удаляет исходник.  
# 6. Привязать handler.namer и handler.rotator.
# 7. Формат: %(asctime)s | %(levelname)s | %(message)s.
# 8. Симуляция: 30 ошибок с паузой.
    

НЕ РАБОТАЕТ!
Кол-во архивов явно больше 3х(выясненно ниже!)
Файл battle.log не удаляется(по логике оно и не может удалиться ротатором.Так как в него идет основной лог.)
NAMER принимает name = 'battle.log.1'(с цифрой на конце)! Специально запринтил
source в ROTATOR передается как battle.log (БЕЗ цифры на конце). Специально запринтил!
Размер MaxBytes = 1*102  - СПЕЦИАЛЬНО уменьшил для наглядности
Количество симуляций СПЕЦИАЛЬНО увеличил
____________________________________
ИТАК ВЫЯСНЕНО!!! NAMER работает так: Если мы создаем с кастомным неймером УНИКАЛЬНЫЕ ИМЕНА файлов(как в случае со временем),
то каждый раз при ротации будут создаваться НОВЫЕ файлы с кастомными именами(их кол-во ограничено только кол-вом общим кол-вом ротаций) и никак не привязано к backupCount  .
А если эти имена будут шаблонными (как в случае с бэкапами log.1,log.2,log.3 и тд), то будет работать как надо(перезаписывая ровно нужное кол-во заданных бекапов- привязано к backupCount)
____________________________________

def namer(name):
    print(f"NAMER: Received name = '{name}'")
    # TODO: разделить name на base и ext
    # splitted_name = os.path.splitext(name)  НЕ РАБОТАЕТ! ДЕЛИТ НА battle.log и индекс 1-....
    splitted_name = name.split('.')
    base = splitted_name[0]
    ext = splitted_name[1]
    index = splitted_name[-1]
    print('LEN', len(splitted_name), 'base=', base, 'ext=', ext, 'index=', index) 
    # TODO: собрать новое имя base + '.' + timestamp + ext
    new_name = f'{base}.{time.strftime('%Y-%m-%d_%H-%M-%S')}.{ext}' 
    # TODO: вернуть новое имя
    print('NAMER: New name = ', new_name)
    return new_name


def rotator(source, dest):
    print(f"ROTATOR: Source file = '{source}', Dest file = '{dest}'")
    try:
        # TODO: открыть source для чтения в бинарном режиме
        with open(source, 'rb') as f:
            # TODO: открыть gzip-архив dest+'.gz' для записи
            with gzip.open(f"{dest}.gz", 'wb') as g:
                # TODO: скопировать данные и удалить source
                g.writelines(line for line in f)
        os.remove(source)  # НЕ РАБОТАЕТ!!!
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)


# TODO: создать RotatingFileHandler:
#   - filename = 'battle.log'
#   - maxBytes = 10*1024
#   - backupCount = 3
handler = RotatingFileHandler(
    'battle.log',
    maxBytes=1 * 102,
    backupCount=3
)
# TODO: присвоить handler.namer = namer и handler.rotator = rotator
handler.namer = namer
handler.rotator = rotator
logger = logging.getLogger('fleet.archive')

# TODO: установить уровень логирования ERROR
logger.setLevel(logging.ERROR)
# TODO: прикрепить handler к logger
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# --- Симуляция: 30 критических ошибок ---
for i in range(50):
    # TODO: вызвать logger.error с текстом "Critical battle error #{i}"
    logger.error(f"Critical battle error #{i}")
    print(f"Simulate critical battle error #{i}")
    time.sleep(0.1)


# if os.path.exists('battle.log'):
#     os.remove('battle.log')


