import re


def extract_product_info(html_content):
    """
    Функция extract_product_info принимает на вход html-страницу с товарами и
    возвращает список продуктов, которые соответствуют следующим критериям:
    - цена меньше 5000 рублей
    - продукт есть в наличии
    """

    affordable_in_stock_products = []
    # TODO: Найдите все блоки продуктов
    product_pattern = r"\<div.*?\>.*?(?<=\<\/p\>.)\</div\>"
    product_blocks = re.findall(product_pattern, html_content, re.DOTALL)
    # название продукта
    title_pattern = re.compile(r"\<h2 class\=\"product-title\"\>(.*?)\<\/h2\>")
    # цена
    price_pattern = re.compile(r"\<span class\=\"price\"\>(.*?)\<\/span\>")
    # скидка
    discount_pattern = re.compile(r"\<span class\=\"discount\"\>(.*?)\<\/span\>")
    # наличие
    stock_pattern = re.compile(r"\<p class\=\"stock\"\>(.*?)\<\/p\>")
    for product_block in product_blocks:
        # print(product_block)
        # print()
        #  Извлеките название продукта
        title_match = title_pattern.search(product_block)
        title = title_match.group(1)
       
        #  Извлеките цену
        price_match = price_pattern.search(product_block)
        price = price_match.group(1)

        #  Извлеките скидку (если есть)
        discount_match = discount_pattern.search(product_block)
        if discount_match:
            discount = discount_match.group(1) if discount_match else 'Нет скидки'

        #  Проверьте наличие
        stock_match = stock_pattern.search(product_block)
        stock = stock_match.group(1)
        # print(title)
        # print(int(price.split()[0]) < 5000)
        # print(stock)
        
        #  Добавьте продукт в результат, если он соответствует критериям(в наличии и стоит меньше 5000 руб.)
        if stock == 'В наличии' and int(price.split()[0]) < 5000:
            affordable_in_stock_products.append({'Название': title, 'Цена': price, 'Скидка': discount, 'Наличие': stock})
    return affordable_in_stock_products


# Пример HTML-контента (в реальном сценарии вы бы читали из файла)
html_content = """
<div class="product-item">
<h2 class="product-title">Смартфон Яблофон 13</h2>
<div class="product-price">
<span class="price">4999 руб.</span>
<span class="discount">-15%</span>
</div>
<p class="stock">В наличии</p>
<p class="description">Отличный смартфон с хорошей камерой</p>
</div>
<div class="product-item">
<h2 class="product-title">Ноутбук ПроБук Z</h2>
<div class="product-price">
<span class="price">75999 руб.</span>
</div>
<p class="stock">В наличии</p>
<p class="description">Мощный ноутбук для профессионалов</p>
</div>
<div class="product-item">
<h2 class="product-title">Планшет Галактика Tab 4</h2>
<div class="product-price">
<span class="price">3999 руб.</span>
<span class="discount">-20%</span>
</div>
<p class="stock">Нет в наличии</p>
<p class="description">Компактный планшет для работы и развлечений</p>
</div>
<div class="product-item">
<h2 class="product-title">Умные часы ФитПро</h2>
<div class="product-price">
<span class="price">2999 руб.</span>
</div>
<p class="stock">В наличии</p>
<p class="description">Отслеживайте свою активность и здоровье</p>
</div>
"""

# Вызов функции и вывод результатов
products = extract_product_info(html_content)
# print(products)
for product in products:
    for key, value in product.items():
        print(f"{key}: {value}")
    print() # Пустая строка для разделения продуктов