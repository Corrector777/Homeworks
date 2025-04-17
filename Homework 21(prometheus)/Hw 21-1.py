from prometheus_client import start_http_server, generate_latest, Counter, Gauge, CONTENT_TYPE_LATEST
# TODO: Импортировать классы Counter и Gauge
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

# TODO: Создать счетчик для отслеживания просмотров страниц
PAGE_VIEWS_COUNTER = Counter('page_views_total', 'Total number of page views')

# TODO: Создать счетчик с метками для отслеживания просмотров конкретных страниц 
PAGE_VIEWS_COUNTER_LABELED = Counter('page_views_by_category_total', 'Total number of page views by category', ['category'])

# TODO: Создать счетчик для отслеживания добавлений товаров в корзину
ADD_CART_COUNTER = Counter('add_to_cart_total', 'Total number of products added to cart')

# TODO: Создать счетчик для отслеживания покупок
PURCHASE_COUNTER = Counter('purchase_total', 'Total number of purchases')

# TODO: Создать измеритель для отслеживания количества активных пользователей
ACTIVE_USERS_GAUGE = Gauge('active_users', 'Number of active users')

# TODO: Создать измеритель для отслеживания среднего размера корзины (количество товаров)
MIDDLE_CART_SIZE_GAUGE = Gauge('middle_cart_size', 'Middle size of cart')


# Функция для симуляции просмотра главной страницы
def simulate_home_page_view():
    print("Пользователь просмотрел главную страницу")
    # TODO: Увеличить счетчик просмотров страниц
    PAGE_VIEWS_COUNTER.inc()
    # TODO: Увеличить счетчик просмотров конкретной страницы (главной)
    PAGE_VIEWS_COUNTER_LABELED.labels(category='home').inc()


# Функция для симуляции просмотра каталога
def simulate_catalog_view():
    print("Пользователь просмотрел каталог товаров")
    # TODO: Увеличить счетчик просмотров страниц
    PAGE_VIEWS_COUNTER.inc()
    # TODO: Увеличить счетчик просмотров конкретной страницы (каталога)
    PAGE_VIEWS_COUNTER_LABELED.labels(category='catalog').inc()


# Функция для симуляции просмотра товара
def simulate_product_view(product_id):
    if product_id not in PRODUCTS:
        print(f"Ошибка: товар с ID {product_id} не найден")
        return
    
    print(f"Пользователь просмотрел товар: {PRODUCTS[product_id]['name']}")
    # TODO: Увеличить счетчик просмотров страниц
    PAGE_VIEWS_COUNTER.inc()
    # TODO: Увеличить счетчик просмотров конкретной страницы (товара)
    PAGE_VIEWS_COUNTER_LABELED.labels(category=PRODUCTS[product_id]['name']).inc()


# Функция для симуляции добавления товара в корзину
def simulate_add_to_cart(product_id):
    if product_id not in PRODUCTS:
        print(f"Ошибка: товар с ID {product_id} не найден")
        return
    
    print(f"Пользователь добавил в корзину: {PRODUCTS[product_id]['name']}")
    # TODO: Увеличить счетчик добавлений в корзину
    ADD_CART_COUNTER.inc()
    
    # Обновляем среднее количество товаров в корзине (для симуляции)
    new_avg = random.uniform(1.5, 4.0)
    print(f"Среднее количество товаров в корзине теперь: {new_avg:.2f}")
    # TODO: Установить новое значение для измерителя среднего размера корзины
    MIDDLE_CART_SIZE_GAUGE.set(new_avg)


# Функция для симуляции оформления заказа
def simulate_purchase():
    print("Пользователь оформил заказ")
    # TODO: Увеличить счетчик покупок
    PURCHASE_COUNTER.inc()


# Функция для симуляции изменения количества активных пользователей
def simulate_active_users_change():
    new_users = random.randint(10, 100)
    print(f"Количество активных пользователей: {new_users}")
    # TODO: Установить новое значение для измерителя активных пользователей
    ACTIVE_USERS_GAUGE.set(new_users)


# Основная функция для симуляции активности на сайте
def simulate_site_activity():
    # Запускаем HTTP-сервер для предоставления метрик Prometheus
    # TODO: Запустить HTTP-сервер на порту 8000
    start_http_server(8000)
    print("Сервер метрик запущен на http://localhost:8000/metrics")
    try:
        while True:
            # Симулируем случайную активность
            action = random.randint(1, 10)
            
            if action <= 3:  # 30% вероятность
                simulate_home_page_view()
            elif action <= 6:  # 30% вероятность
                simulate_catalog_view()
            elif action <= 8:  # 20% вероятность
                product_id = random.randint(1, len(PRODUCTS))
                simulate_product_view(product_id)
            elif action <= 9:  # 10% вероятность
                product_id = random.randint(1, len(PRODUCTS))
                simulate_add_to_cart(product_id)
            else:  # 10% вероятность
                simulate_purchase()
            
            # Периодически обновляем количество активных пользователей
            if random.random() < 0.2:  # 20% вероятность при каждой итерации
                simulate_active_users_change()
            
            # Пауза между действиями
            time.sleep(random.uniform(0.5, 2.0))
            
    except KeyboardInterrupt:
        print("Симуляция остановлена")

if __name__ == "__main__":
    simulate_site_activity()


