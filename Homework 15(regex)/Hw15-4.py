import re


def standardize_filenames(filenames):
    standardized_names = []
    doc_type_map = {
'отчет': 'ОТЧЕТ',
'договор': 'ДОГОВОР',
'счет': 'СЧЕТ',
'презентация': 'ПРЕЗЕНТАЦИЯ',
'документация': 'ДОКУМЕНТАЦИЯ',
'анализ': 'АНАЛИЗ'
}
# Скомпилированные регулярные выражения для оптимизации
    # TODO: Создайте регулярные выражения для извлечения типа документа
    type_pattern = re.compile(r"документация|отчет|договор|счет|презентация|анализ", re.IGNORECASE)
    # Можно добавить другие типы по необходимости
        
    # TODO: Создайте регулярное выражение для извлечения даты
    date_pattern = re.compile(r'(\d{2}).(\d{2}).(\d{4})')
    # print(date_pattern)
    # TODO: Создайте регулярное выражение для извлечения ID проекта
    project_pattern = re.compile(r'(?:проект[ау]?\s+|по_проекту_)?([A-Z]{3}\d{3})')
    # print(project_pattern)
    # TODO: Создайте регулярное выражение для извлечения автора/отдела    
    department_pattern = re.compile(r'отдел_аналитики|маркетинг|отдел_продаж|отдел_разработки', re.IGNORECASE)
    author_in_parentheses = re.compile(r'\(([а-яА-Я]+)\)')
    author_in_begin = re.compile(r'^([а-яА-Я]+)_')
    author_after_for = re.compile(r'для.([а-яА-Я]+)+')
    athor_in_end = re.compile(r'\s+([а-яА-Я]+)\.')
    for filename in filenames:
        # print(filename)
        # Извлекаем расширение файла
        extension = filename.split('.')[-1]
        # print(extension)
        # TODO: Определите тип документа
        doc_type_match = type_pattern.search(filename)
        if doc_type_match:
            found_type = doc_type_match.group(0).lower()
            doc_type = doc_type_map.get(found_type, found_type.upper())   
        else:
            doc_type = "НЕИЗВЕСТЕН"
        # print(doc_type)
        # TODO: Извлеките дату
        date = date_pattern.search(filename)
        if date:
            date = f"{date.group(3)}-{date.group(2)}-{date.group(1)}"
        else:
            date = "БЕЗ-ДАТЫ"
        # print(date)
        # TODO: Извлеките ID проекта
        project_match = project_pattern.search(filename)
        # 7. Использование современных языковых возможностей
        #     Конструкция next((g for g in project_match.groups() if g))
        #     демонстрирует элегантное применение генераторов и функции next() для поиска
        #     первого непустого значения.
        # print('project_id', project_match)
        # if project_match:
        #     project_id = next(g for g in project_match.groups() if g)
        # else:
        #     project_id = "НЕИЗВЕСТЕН"

        # при упрощенном регулярном выражении(как сейчас):
        project_id = project_match.group(1) if project_match else "НЕИЗВЕСТЕН"    
        # print(project_id)
        # TODO: Извлеките автора/отдел
        for pattern in [author_in_parentheses, author_in_begin, author_after_for, athor_in_end]:
            match = pattern.search(filename)
            if match:
                author = match.group(1)
                break
        department = department_pattern.search(filename)
        if department:
            department_author = department.group(0).upper()
        elif author:
            department_author = author.upper()
        else:
            department_author = "НЕИЗВЕСТЕН"
        # print(department_author)
        # Формируем новое имя файла
        new_filename = f"{doc_type}_{date}_{project_id}_{department_author}.{extension}"

        standardized_names.append({
        "original": filename,
        "new": new_filename
        })
    return standardized_names


# Пример списка имен файлов
filenames = [
    "отчет от 23-04-2023 для проекта XYZ123 (Иванов).docx",
    "договор_с_клиентом_от 15-01-2023_Отдел_продаж.pdf",
    "счет-№45-67-от-10.05.2023-для-ABC-Corp.pdf",
    "Презентация продукта v2 (дата 30-06-2023) Маркетинг.pptx",
    "Иванов_отчет_по_проекту_DEF456_05_04_2023.xlsx",
    "12.03.2023_Отдел_разработки_Техническая_документация.docx",
    "анализ_рынка(без_даты)_отдел_аналитики.xlsx"
]
# Вызов функции и вывод результатов
results = standardize_filenames(filenames)
for result in results:
    print(f"Исходное имя: {result['original']}")
    print(f"Новое имя: {result['new']}")
    print() # Пустая строка для разделения