from prometheus_client import start_http_server, Counter, Gauge, Histogram, Summary
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


# Источники трафика (маркетинговые кампании)
TRAFFIC_SOURCES = [
    "organic_search",
    "paid_search",
    "social_media",
    "email_campaign",
    "affiliate",
    "direct"
]


# Базовые счетчики для событий
# Счетчик просмотров товаров с метками категории и источника трафика
PRODUCT_VIEWS = Counter(
    'product_views_total', 
    'Количество просмотров товаров по категориям и источникам трафика', 
    ['category', 'source']
)

# Счетчик добавлений в корзину с метками категории
CART_ADDITIONS = Counter(
    'cart_additions_total', 
    'Количество добавлений товаров в корзину по категориям', 
    ['category']
)

# Счетчик покупок с метками категории и источника трафика
PURCHASES = Counter(
    'purchases_total', 
    'Количество совершенных покупок по категориям и источникам трафика', 
    ['category', 'source']
)

# Счетчик отказов от корзины с метками категории
CART_ABANDONMENT = Counter(
    'cart_abandonment_total', 
    'Количество отказов от корзины по категориям', 
    ['category']
)

# TODO: Создать счетчик для суммарной стоимости покупок
SUMMURY_PURCHASES_COUNTER = Counter(
    'summury_purchases_total', 
    'Суммарная стоимость покупок'
)
 
# TODO: Создать гистограмму для распределения стоимости заказов
ORDERS_PRICE_HISTOGRAM = Histogram(
    'orders_price', 
    'Распределение стоимости заказов', 
    buckets=[10000, 15000, 35000, 50000, 100000, 400000, 1000000, float('inf')]
)

# TODO: Создать измеритель для конверсии просмотра в покупку (для каждой категории и источника)
VIEWS_CONVERSIONS_GAUGE_LABELED = Gauge('views_conversion_rate', 'Конверсия просмотров в покупки по категориям и источникам', ['category', 'source'])    

# TODO: Создать измеритель для конверсии добавления в корзину в покупку
CART_CONVERSIONS_GAUGE_LABELED = Gauge('cart_conversion_rate', 'Конверсия добавления в корзину в покупку по категориям', ['category'])

# TODO: Создать измеритель для показателя отказов от корзины
CART_ABANDONMENT_GAUGE_lABELED = Gauge('cart_abandonment_gauge', 'Показатель отказов от корзины по категориям', ['category'])

# TODO: Создать измеритель для средней стоимости заказа
AVERAGE_ORDER_PRICE_GAUGE_LABELED = Gauge('average_order_price', 'Средняя стоимость заказа по источникам', ['source'])

# Словари для хранения промежуточных значений (в реальном приложении это было бы в базе данных)
category_views = {category: {source: 0 for source in TRAFFIC_SOURCES} for category in set(product["category"] for product in PRODUCTS.values())}
category_purchases = {category: {source: 0 for source in TRAFFIC_SOURCES} for category in set(product["category"] for product in PRODUCTS.values())}
category_cart_adds = {category: 0 for category in set(product["category"] for product in PRODUCTS.values())}
category_cart_abandons = {category: 0 for category in set(product["category"] for product in PRODUCTS.values())}
source_revenue = {source: 0 for source in TRAFFIC_SOURCES}
source_purchases = {source: 0 for source in TRAFFIC_SOURCES}


# Функция для симуляции просмотра товара
def simulate_product_view():
    # Выбираем случайный товар и источник трафика
    product_id = random.randint(1, len(PRODUCTS))
    product = PRODUCTS[product_id]
    category = product["category"]
    source = random.choice(TRAFFIC_SOURCES)
    print(f"Просмотр товара: {product['name']} (Категория: {category}, Источник: {source})")
    
    # Увеличиваем счетчик просмотров
    PRODUCT_VIEWS.labels(category=category, source=source).inc()
    
    # Обновляем внутренний счетчик для расчета конверсии
    category_views[category][source] += 1
    
    # TODO: Обновить коэффициент конверсии для этой категории и источника
    views = category_views[category][source]
    purchases = category_purchases[category][source]
    if views > 0:
        conversion_rate = round((purchases / views) * 100, 2)
    else:
        conversion_rate = 0
    VIEWS_CONVERSIONS_GAUGE_LABELED.labels(category=category, source=source).set(conversion_rate)


# Функция для симуляции добавления товара в корзину
def simulate_add_to_cart():
    # Выбираем случайный товар
    product_id = random.randint(1, len(PRODUCTS))
    product = PRODUCTS[product_id]
    category = product["category"]
    
    print(f"Добавление в корзину: {product['name']} (Категория: {category})")
    
    # Увеличиваем счетчик добавлений в корзину
    CART_ADDITIONS.labels(category=category).inc()
    
    # Обновляем внутренний счетчик
    category_cart_adds[category] += 1
    
    # TODO: Обновить коэффициент конверсии корзины в покупку 
    cart_adds = category_cart_adds[category]
    purchases = sum(category_purchases[category].values())
    if cart_adds > 0:
        conversatoins_rate = round((purchases / cart_adds) * 100, 2)
    else:
        conversatoins_rate = 0
    CART_CONVERSIONS_GAUGE_LABELED.labels(category=category).set(conversatoins_rate)


# Функция для симуляции отказа от корзины
def simulate_cart_abandonment():
    # Выбираем случайный товар, от корзины с которым пользователь отказался
    product_id = random.randint(1, len(PRODUCTS))
    product = PRODUCTS[product_id]
    category = product["category"]
    
    print(f"Отказ от корзины с товаром: {product['name']} (Категория: {category})")
    
    # Увеличиваем счетчик отказов от корзины
    CART_ABANDONMENT.labels(category=category).inc()
    
    # Обновляем внутренний счетчик
    category_cart_abandons[category] += 1
    # TODO: Обновить показатель отказов от корзины для этой категории
    abandons = category_cart_abandons[category]
    adds = category_cart_adds[category]
    if adds > 0:
        abandonment_rate = round((abandons / adds) * 100, 2)
    else:
        abandonment_rate = 0    
    CART_ABANDONMENT_GAUGE_lABELED.labels(category=category).set(abandonment_rate)


# Функция для симуляции покупки
def simulate_purchase():
    # Выбираем случайный товар
    product_id = random.randint(1, len(PRODUCTS))
    product = PRODUCTS[product_id]
    category = product["category"]
    price = product["price"]
    source = random.choice(TRAFFIC_SOURCES)
    
    # Иногда покупают несколько товаров
    quantity = random.choices([1, 2, 3], weights=[0.7, 0.2, 0.1])[0]
    total_price = price * quantity
    
    print(f"Покупка: {quantity}x {product['name']} за {total_price} руб. (Категория: {category}, Источник: {source})")
    
    # Увеличиваем счетчик покупок
    PURCHASES.labels(category=category, source=source).inc()
    
    # TODO: Увеличить счетчик выручки
    SUMMURY_PURCHASES_COUNTER.inc(total_price)
    
    # TODO: Записать стоимость заказа в гистограмму
    ORDERS_PRICE_HISTOGRAM.observe(total_price)
    
    # Обновляем внутренние счетчики для расчетов
    category_purchases[category][source] += 1
    source_revenue[source] += total_price
    source_purchases[source] += 1
    
    # TODO: Обновить среднюю стоимость заказа для этого источника
    avarange_order_price = round(source_revenue[source] / source_purchases[source], 2)
    AVERAGE_ORDER_PRICE_GAUGE_LABELED.labels(source=source).set(avarange_order_price)
    
    # TODO: Обновить конверсию просмотра в покупку
    views = category_views[category][source]
    if views > 0:
        conversatoins_rate = round((source_purchases[source] / views) * 100, 2)
    else:
        conversatoins_rate = 0
    VIEWS_CONVERSIONS_GAUGE_LABELED.labels(category=category, source=source).set(conversatoins_rate)


    # TODO: Обновить конверсию корзины в покупку и показатель отказов для категории
    cart_adds = category_cart_adds[category]
    purchases = sum(category_purchases[category].values())
    cart_abandons = category_cart_abandons[category]
    if cart_adds > 0:
        conversatoins_rate = round((purchases / cart_adds) * 100, 2)
        abandonment_rate = round((cart_abandons / cart_adds) * 100, 2)
    else:
        conversatoins_rate = 0
        abandonment_rate = 0
    CART_CONVERSIONS_GAUGE_LABELED.labels(category=category).set(conversatoins_rate)    
    CART_ABANDONMENT_GAUGE_lABELED.labels(category=category).set(abandonment_rate)


# Основная функция для симуляции активности на сайте
def simulate_site_activity():
    # Запускаем HTTP-сервер для предоставления метрик Prometheus
    start_http_server(8000)
    print("Сервер метрик запущен на http://localhost:8000/metrics")
    
    try:
        while True:
            # Симулируем случайную активность
            action = random.randint(1, 20)
            
            if action <= 10:  # 50% вероятность
                simulate_product_view()
            elif action <= 14:  # 20% вероятность
                simulate_add_to_cart()
            elif action <= 17:  # 15% вероятность
                simulate_cart_abandonment()
            elif action <= 19:  # 5% вероятность !!уменьшил вероятность покупки для конверсии СПЕЦИАЛЬНО!!!
                simulate_purchase()
            
            # Пауза между действиями
            time.sleep(random.uniform(0.2, 0.8))
            
    except KeyboardInterrupt:
        print("Симуляция остановлена")


if __name__ == "__main__":
    simulate_site_activity()