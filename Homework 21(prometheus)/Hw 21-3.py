from prometheus_client import start_http_server, Counter, Gauge, Histogram
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

# Список категорий товаров
CATEGORIES = ["Телефоны", "Компьютеры", "Аудио", "Планшеты", "Гаджеты"]

# Методы оплаты
PAYMENT_METHODS = ["Кредитная карта", "PayPal", "Банковский перевод", "Наложенный платеж", "Электронный кошелек"]

# TODO: Создать счетчик просмотров товаров с метками по категориям
PRODUCTS_VEWS_COUNTER_LABELED = Counter('products_views_by_category', 'Total number of products views by category', ['category'])

# TODO: Создать счетчик добавлений в корзину с метками по категориям
ADD_CART_COUNTER_LABELED = Counter('add_to_cart_by_category', 'Total number of products added to cart by category', ['category'])

# TODO: Создать счетчик покупок с метками по категориям и методу оплаты
PURCHASE_COUNTER_LABELED = Counter('purchase_by_category_and_payment_method', 'Total number of purchases by category and payment method', ['category', 'payment_method'])

# TODO: Создать счетчик ошибок при оплате с метками по методу оплаты и типу ошибки
PAYMENT_ERROR_TYPES_COUNTER_LABELED = Counter('payment_errors_by_payment_method_and_error_type', 'Total number of payment errors by payment method and error type', ['payment_method', 'error_type'])

# TODO: Создать гистограмму времени оформления заказа с метками по методу оплаты
ORDER_PROCESSING_TIME_HISTOGRAM_LABELED = Histogram('order_processing_time_by_payment_method', 'Histogram of order processing time by payment method', ['payment_method'])

# Возможные типы ошибок оплаты
PAYMENT_ERROR_TYPES = [
    "insufficient_funds", 
    "card_declined", 
    "network_error",
    "invalid_details",
    "timeout"
]

# Функция для симуляции просмотра товара по категории
def simulate_product_view():
    # Выбираем случайный товар
    product_id = random.randint(1, len(PRODUCTS))
    product = PRODUCTS[product_id]
    category = product["category"]
    
    print(f"Просмотр товара: {product['name']} (Категория: {category})")
    
    # TODO: Увеличить счетчик просмотров товаров по категории

# Функция для симуляции добавления товара в корзину
def simulate_add_to_cart():
    # Выбираем случайный товар
    product_id = random.randint(1, len(PRODUCTS))
    product = PRODUCTS[product_id]
    category = product["category"]
    
    print(f"Добавление в корзину: {product['name']} (Категория: {category})")
    
    # TODO: Увеличить счетчик добавлений в корзину по категории
    ADD_CART_COUNTER_LABELED.labels(category=category).inc()


# Функция для симуляции оформления заказа с определенным методом оплаты
def simulate_checkout():
    # Выбираем случайный товар для покупки
    product_id = random.randint(1, len(PRODUCTS))
    product = PRODUCTS[product_id]
    category = product["category"]
    
    # Выбираем случайный метод оплаты
    payment_method = random.choice(PAYMENT_METHODS)
    
    print(f"Оформление заказа: {product['name']} (Категория: {category})")
    print(f"Метод оплаты: {payment_method}")
    
    # Засекаем время начала оформления
    start_time = time.time()
    
    # Имитация процесса оформления заказа
    print("Обработка заказа...")
    
    # Разное время обработки для разных методов оплаты
    if payment_method == "Кредитная карта":
        delay = random.uniform(0.5, 1.5)
    elif payment_method == "PayPal":
        delay = random.uniform(1.0, 2.0)
    elif payment_method == "Банковский перевод":
        delay = random.uniform(2.0, 4.0)
    elif payment_method == "Наложенный платеж":
        delay = random.uniform(0.3, 0.8)
    else:  # Электронный кошелек
        delay = random.uniform(0.7, 1.7)
    
    time.sleep(delay)
    
    # Определяем, будет ли ошибка при оплате
    success = random.random() > 0.2  # 20% вероятность ошибки
    
    duration = time.time() - start_time
    
    if success:
        print(f"Заказ успешно оформлен за {duration:.3f} секунд")
        # TODO: Увеличить счетчик покупок с метками категории и метода оплаты
        PURCHASE_COUNTER_LABELED.labels(category=category, payment_method=payment_method).inc()
    else:
        # Выбираем случайный тип ошибки
        error_type = random.choice(PAYMENT_ERROR_TYPES)
        print(f"⚠️ Ошибка при оплате: {error_type}")
        # TODO: Увеличить счетчик ошибок с метками метода оплаты и типа ошибки
        PAYMENT_ERROR_TYPES_COUNTER_LABELED.labels(payment_method=payment_method, error_type=error_type).inc()
    
    # TODO: Записать длительность оформления заказа в гистограмму с меткой метода оплаты
    ORDER_PROCESSING_TIME_HISTOGRAM_LABELED.labels(payment_method=payment_method).observe(duration)

# Основная функция для симуляции активности на сайте
def simulate_site_activity():
    # Запускаем HTTP-сервер для предоставления метрик Prometheus
    start_http_server(8000)
    print("Сервер метрик запущен на http://localhost:8000/metrics")
    
    try:
        while True:
            # Симулируем случайную активность
            action = random.randint(1, 10)
            
            if action <= 5:  # 50% вероятность
                simulate_product_view()
            elif action <= 8:  # 30% вероятность
                simulate_add_to_cart()
            else:  # 20% вероятность
                simulate_checkout()
            
            # Пауза между действиями
            time.sleep(random.uniform(0.3, 1.0))
            
    except KeyboardInterrupt:
        print("Симуляция остановлена")

if __name__ == "__main__":
    simulate_site_activity()