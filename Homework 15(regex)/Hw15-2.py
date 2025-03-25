import re
# 1. Напишите скрипт, который проанализирует лог-файл веб-сервера
# 2. Найдите все POST-запросы к endpoint'ам, начинающимся с /api/
# 3. Отфильтруйте только запросы с IP-адресов, начинающихся с 192.168.1.
# 4. Выведите результат в формате: "Дата и время | IP | Endpoint | Статус | SQL-инъекция [да/нет]"


def analyze_web_logs(log_lines):
    suspicious_activities = []
    # Напишите регулярное выражение для парсинга строк лога
    log_pattern = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) \[(.*?)\] (.+) (\d{3}) ")
    # Напишите регулярное выражение для проверки SQL-инъекций
    sql_injection_pattern = re.compile(r"SELECT|INSERT|UPDATE|DELETE|DROP|UNION|--|;")
    for line in log_lines:
        match = log_pattern.match(line)
        # print(match.groups())
        if match:
            date_time, ip, method, endpoint, status = match.groups()
            # print(f'{ip} | {method} | {endpoint} |{status}')
            # Проверьте, является ли запрос POST-запросом к /api/
            if method == 'POST' and endpoint.startswith('/api/'):
                # Проверьте, начинается ли IP с 192.168.1.
                if ip.startswith('192.168.1.'):
                    # print(ip, method, endpoint)
                    # Проверьте на наличие SQL-инъекций
                    sql = sql_injection_pattern.search(endpoint)
                    # print(sql)
                    suspicious_activities.append(f"{date_time} | {ip} | {method} | {endpoint} | {status} | SQL-инъекция: {'да' if sql else 'нет'}")
        pass
    return suspicious_activities

log_lines = [
"2023-07-15 08:42:15 - 192.168.1.105 [GET] /index.html 200 \"Mozilla/5.0\"",
"2023-07-15 09:15:22 - 192.168.1.105 [POST] /api/users 201 \"PostmanRuntime/7.29.0\"",
"2023-07-15 09:17:44 - 192.168.1.106 [POST] /api/data?query=SELECT%20*%20FROM%20users 403 \"Bad-Actor/1.0\"",
"2023-07-15 10:22:31 - 10.0.0.15 [POST] /api/products 201 \"Mozilla/5.0\"",
"2023-07-15 11:05:18 - 192.168.1.107 [GET] /images/logo.png 200 \"Mozilla/5.0\"",
"2023-07-15 11:36:49 - 192.168.1.108 [POST] /api/admin/users?query=DROP%20TABLE%20users 403 \"Bad-Actor/1.0\"",
"2023-07-15 12:41:27 - 192.168.1.105 [POST] /login 200 \"Mozilla/5.0\""]


# Вызов функции и вывод результатов
results = analyze_web_logs(log_lines)
for result in results:
    print(result)   