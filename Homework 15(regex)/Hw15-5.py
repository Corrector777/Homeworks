import re


def detect_sql_injection(query_string):
    result = {"safe": True, "details": []}
    # Скомпилированные регулярные выражения для оптимизации
    # TODO: Регулярное выражение для обнаружения базовых SQL-инъекций
    basic_injection_pattern = re.compile(r'SELECT.*\=\'\w+\'|INSERT|UPDATE\w+user.+|DELETE|DROP.*user.+')
    # TODO: Регулярное выражение для обнаружения комментариев SQL
    comment_injection_pattern = re.compile(r'--|/\*.*?\*/')
    # TODO: Регулярное выражение для обнаружения UNION-атак
    union_injection_pattern = re.compile(r'UNION.+FROM.*')
    # TODO: Регулярное выражение для обнаружения условий OR/AND в необычном контексте
    logical_injection_pattern = re.compile(r'OR.*|AND.*')
    # TODO: Регулярное выражение для обнаружения модификации данных
    data_modification_pattern = re.compile(r'UPDATE.*\=\'\w+\'')
    # Проверка на различные типы инъекций
    # TODO: Реализуйте проверки и заполните result
    basic = basic_injection_pattern.search(query_string)
    comment = comment_injection_pattern.search(query_string)
    union = union_injection_pattern.search(query_string)
    logical = logical_injection_pattern.search(query_string)
    data = data_modification_pattern.search(query_string)

    if basic:
        result["safe"] = False
        result["details"].append({
            "type": "Базовая инъекция",
            "found": basic.group(),
            "risk_level": "Низкий"
        })
    if comment:
        result["safe"] = False
        result["details"].append({
            "type": "Комментарий SQL",
            "found": comment.group(),
            "risk_level": "Высокий"
        })
    if union:
        result["safe"] = False
        result["details"].append({
            "type": "UNION-атака",
            "found": union.group(),
            "risk_level": "Критичекий"
        })
    if logical:
        result["safe"] = False
        result["details"].append({
            "type": "Логическая инъекция",
            "found": logical.group(),
            "risk_level": "Критический"
        })
    if data:
        result["safe"] = False
        result["details"].append({
            "type": "Модификация данных",
            "found": data.group(),
            "risk_level": "Критический"
        })

    return result


# Пример запросов для проверки
queries = [
"username=johndoe&password=12345",
"username=admin&password=password' OR '1'='1'",
"username=guest&password=123'; DROP TABLE users; --",
"search=smartphone&sort=price; UNION SELECT username,password FROM users",
"id=15; SELECT * FROM users WHERE username='admin'--&category=electronics",
"product_id=7 OR 1=1",
"email=test@test.com'; UPDATE users SET role='admin' WHERE email='test@test.com"
]
# Проверка запросов и вывод результатов
for query in queries:
    result = detect_sql_injection(query)
    print(f'"{query}" - ', end="")
    if result["safe"]:
        print("Безопасный запрос")
    else:
        print("ВНИМАНИЕ: Возможная SQL-инъекция!")
        for detail in result["details"]:
            print(f"- Тип: {detail['type']}")
            print(f"- Обнаружено: \"{detail['found']}\"")
            print(f"- Уровень риска: {detail['risk_level']}")
    print() # Пустая строка для разделения