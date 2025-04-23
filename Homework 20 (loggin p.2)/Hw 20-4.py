import logging, logging.handlers, multiprocessing

## **Задание 4. “Собираем весь флот”**
# **Сюжет:**
# Архивариус агрегирует логи с трёх подсистем USS “Энтерпрайз” (двигатели, оружие, навигация), приходящие параллельно. 
# Центральный процесс‑слушатель безопасно ротирует общий файл.
# **ТЗ:**

# 1. listener_configurer():
#     - Создать RotatingFileHandler('fleet.log', maxBytes=100*1024, backupCount=5).
#     - Установить форматтер и прикрепить к корневому логгеру.
        
# 2. listener_process(queue):
#     - Цикл: record = queue.get() до None.
#     - Если record is None → break.
#     - Иначе: logging.getLogger(record.name).handle(record).


def listener_configurer():
    root = logging.getLogger()
    # TODO: создать обработчик с ротацией по размеру и задать формат
    handler = logging.handlers.RotatingFileHandler(
        'fleet.log',
        maxBytes=100*1024,
        backupCount=5   
    )
    # TODO: добавить его в корневой логгер
    root.addHandler(handler)


def listener_process(queue):
    listener_configurer()
    while True:
        record = queue.get()
        # TODO: если record is None — выйти из цикла
        if record is None:
            break
        # ну это все ваще непонятно)) да и рановато. инфы в уроке нет-на будущее, видать... 
        logger = logging.getLogger(record.name)
        logger.handle(record) 


### **worker.py**

# 1. worker_configurer(queue):
#     - Создать QueueHandler(queue), прикрепить к корню, setLevel(DEBUG).
        
    
# 2. worker_process(queue, name):
#     - Вызывать worker_configurer.    
#     - logger = logging.getLogger(f'process.{name}').     
#     - 20 сообщений с паузой 0.1 с.
        
    
# 3. В if __name__ == '__main__':
#     - Создать очередь, запустить listener-процесс, запустить три worker-процесса для engines, weapons, navigation.     
#     - Дождаться join() всех, послать None, дождаться listener.
        
    
import logging, logging.handlers, multiprocessing, time


def worker_configurer(queue):
    # TODO: создать и прикрепить QueueHandler, установить level=DEBUG
    handler = logging.handlers.QueueHandler(queue)
    root = logging.getLogger()
    root.addHandler(handler)
    root.setLevel(logging.DEBUG)


def worker_process(queue, name):
    worker_configurer(queue)
    logger = logging.getLogger(f'process.{name}')
    # --- Симуляция: 20 сообщений от подсистемы ---
    for i in range(20):
        # TODO: вызвать logger.info(f"{name}: message #{i}")
        logger.info(f"{name}: message #{i}")    
        print(f"{name}: simulated log #{i}")
        time.sleep(0.1)


if __name__ == '__main__':
    # TODO: создать multiprocessing.Queue()
    queue = multiprocessing.Queue()
    # TODO: запустить listener_process в отдельном процессе
    listener = multiprocessing.Process(
        target=listener_process,
        args=(queue,)
        )
    listener.start()
    # TODO: запустить три worker-процесса ('engines','weapons','navigation')
    workers = ['engines', 'weapons', 'navigation']
    engines = multiprocessing.Process(
        target=worker_process,
        args=(queue, 'engines'))
    weapons = multiprocessing.Process(
        target=worker_process,
        args=(queue, 'weapons'))
    navigation = multiprocessing.Process(
        target=worker_process,
        args=(queue, 'navigation'))    
    engines.start()
    weapons.start()
    navigation.start()
    # TODO: дождаться их завершения, отправить None в очередь и дождаться listener
    for proccess in [engines, weapons, navigation]:
        proccess.join()
    queue.put(None)
    listener.join()


  
