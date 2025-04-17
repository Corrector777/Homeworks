from prometheus_client import start_http_server, Counter, Gauge, Histogram
# TODO: Импортировать класс Histogram
import time
import random

# Товары в магазине (для симуляции)
PRODUCTS = {
    1: {"name": "Смартфон Galaxy X", "price": 49999, "category": "Телефоны"},
    2: {"name": "Ноутбук ProBook", "price": 89999, "category": "Компьютеры"},
    3: {"name": "Наушники SoundMax", "price": 7999, "category": "Аудио"},
    4: {"name": "Планшет TabPro", "price": 34999, "category": "Планшеты"},
    5: {"name": "Умные часы FitWatch", "price": 12999, "category": "Гаджеты"}
}

# Счетчик просмотров страниц
PAGE_VIEWS = Counter('page_views_total', 'Количество просмотров страниц')

# Счетчик покупок
PURCHASES = Counter('purchases_total', 'Количество совершенных покупок')

# TODO: Создать гистограмму для измерения времени загрузки страницы
# Определите подходящие границы корзин (buckets)
PAGE_LOAD_TIME_HISTOGRAM = Histogram('page_load_time', 'Page load time in seconds', buckets=[0.1, 0.5, 1.0, 2.5, 5, float('inf')])

# TODO: Создать гистограмму для измерения времени поиска товаров
PRODUCTS_SEARCH_TIME_HISTOGRAM = Histogram('products_search_time', 'Products search time in seconds', buckets=[0.1, 0.5, 1.0, 2.5, 3, 4, float('inf')])

# TODO: Создать гистограмму для измерения времени оформления заказа 
ORDER_PROCESSING_TIME_HISTOGRAM = Histogram('order_processing_time', 'Order processing time in seconds', buckets=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, float('inf')])

# TODO: Создать гистограмму для измерения времени загрузки каталога
CATALOG_LOAD_TIME_HISTOGRAM = Histogram('catalog_load_time', 'Catalog load time in seconds', buckets=[0.1, 0.5, 1.0, 2.5, 5, float('inf')])

# Функция для симуляции загрузки страницы товара
def simulate_product_page_load(product_id):
    if product_id not in PRODUCTS:
        print(f"Ошибка: товар с ID {product_id} не найден")
        return
    
    print(f"Загрузка страницы товара: {PRODUCTS[product_id]['name']}")
    
    # Симулируем время загрузки
    start_time = time.time()
    
    # Имитация работы (случайная задержка)
    # Для некоторых товаров иногда происходит долгая загрузка
    if random.random() < 0.1:  # 10% вероятность медленной загрузки
        delay = random.uniform(1.0, 3.0)  # Долгая загрузка (1-3 секунды)
        print(f"⚠️ Медленная загрузка страницы товара!")
    else:
        delay = random.uniform(0.1, 0.5)  # Нормальная загрузка (0.1-0.5 секунды)
    
    time.sleep(delay)
    
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"Страница товара загружена за {duration:.3f} секунд")
    
    # TODO: Зарегистрировать длительность в гистограмме
    PAGE_LOAD_TIME_HISTOGRAM.observe(duration)
    
    # Увеличиваем счетчик просмотров
    PAGE_VIEWS.inc()

# Функция для симуляции поиска товаров
def simulate_product_search(query):
    print(f"Поиск товаров по запросу: '{query}'")
    
    # Засекаем время начала поиска
    start_time = time.time()
    
    # Имитация поиска (случайная задержка)
    # Некоторые поисковые запросы выполняются дольше
    if len(query) > 10 or random.random() < 0.2:  # Длинный запрос или 20% вероятность
        delay = random.uniform(0.8, 2.0)  # Медленный поиск
        print(f"⚠️ Сложный поисковый запрос, требуется больше времени!")
    else:
        delay = random.uniform(0.2, 0.7)  # Нормальный поиск
    
    time.sleep(delay)
    
    # Симулируем результаты поиска
    results_count = random.randint(0, 5)
    
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"Поиск выполнен за {duration:.3f} секунд. Найдено товаров: {results_count}")
    
    # TODO: Зарегистрировать длительность в гистограмме
    PRODUCTS_SEARCH_TIME_HISTOGRAM.observe(duration)

# Функция для симуляции загрузки каталога
def simulate_catalog_load():
    print("Загрузка каталога товаров")
    
    # Засекаем время начала загрузки
    start_time = time.time()
    
    # Имитация загрузки каталога (случайная задержка)
    # Иногда каталог загружается медленно из-за большого количества товаров
    if random.random() < 0.15:  # 15% вероятность медленной загрузки
        delay = random.uniform(1.2, 2.5)  # Медленная загрузка
        print(f"⚠️ Медленная загрузка каталога!")
    else:
        delay = random.uniform(0.3, 0.9)  # Нормальная загрузка
    
    time.sleep(delay)
    
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"Каталог загружен за {duration:.3f} секунд")
    
    # TODO: Зарегистрировать длительность в гистограмме
    CATALOG_LOAD_TIME_HISTOGRAM.observe(duration)
    
    # Увеличиваем счетчик просмотров
    PAGE_VIEWS.inc()

# Функция для симуляции оформления заказа
def simulate_checkout():
    print("Начало оформления заказа")
    
    # Засекаем время начала оформления
    start_time = time.time()
    
    # Имитация процесса оформления заказа (несколько шагов)
    print("1. Проверка корзины...")
    time.sleep(random.uniform(0.1, 0.3))
    
    print("2. Заполнение данных доставки...")
    time.sleep(random.uniform(0.3, 0.6))
    
    print("3. Выбор способа оплаты...")
    time.sleep(random.uniform(0.2, 0.4))
    
    # Иногда процесс оплаты занимает больше времени
    if random.random() < 0.25:  # 25% вероятность задержки
        print("⚠️ Задержка при обработке платежа!")
        time.sleep(random.uniform(1.0, 3.0))
    else:
        print("4. Обработка платежа...")
        time.sleep(random.uniform(0.4, 0.8))
    
    print("5. Завершение заказа...")
    time.sleep(random.uniform(0.1, 0.3))
    
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"Заказ оформлен за {duration:.3f} секунд")
    
    # TODO: Зарегистрировать длительность в гистограмме
    ORDER_PROCESSING_TIME_HISTOGRAM.observe(duration)
    
    # Увеличиваем счетчик покупок
    PURCHASES.inc()

# Основная функция для симуляции активности на сайте
def simulate_site_activity():
    # Запускаем HTTP-сервер для предоставления метрик Prometheus
    start_http_server(8000)
    print("Сервер метрик запущен на http://localhost:8000/metrics")
    
    try:
        while True:
            # Симулируем случайную активность
            action = random.randint(1, 10)
            
            if action <= 4:  # 40% вероятность
                product_id = random.randint(1, len(PRODUCTS))
                simulate_product_page_load(product_id)
            elif action <= 7:  # 30% вероятность
                simulate_catalog_load()
            elif action <= 9:  # 20% вероятность
                search_terms = ["смартфон", "наушники", "планшет", "ноутбук", "часы", 
                              "беспроводные наушники для телефона", "игровой ноутбук"]
                query = random.choice(search_terms)
                simulate_product_search(query)
            else:  # 10% вероятность
                simulate_checkout()
            
            # Пауза между действиями
            time.sleep(random.uniform(0.5, 1.5))
            
    except KeyboardInterrupt:
        print("Симуляция остановлена")

if __name__ == "__main__":
    simulate_site_activity()