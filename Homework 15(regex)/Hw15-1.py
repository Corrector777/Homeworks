import re


def extract_megacorp_emails(text):
    result = []
    # TODO: Напишите регулярное выражение для поиска email-адресов
    email_pattern = r"(?:\w+|\w+\.\w+)(?:@\w+\.\w{3})"
    # TODO: Найдите все email-адреса в тексте
    all_emails = re.findall(email_pattern, text)
    # TODO: Отфильтруйте только megacorp.com адреса
    megacorp_emails = [email for email in all_emails if email.endswith("@megacorp.com")] 
    # TODO: Извлеките имена пользователей и сформируйте результат
    for email in megacorp_emails:
        name = email.split("@")[0]
        result.append(f'Имя пользователя: {name}, Email: {email}')
    return result


# Текст из файла (в реальном сценарии вы бы читали это из файла)
email_text = """
    От: marketing@techguru.com
    Кому: clients@techguru.com
    Тема: Важное сообщение для наших партнеров!
    Уважаемые партнеры,
    Просим обновить ваши контактные данные в нашей системе.
    - john.doe@megacorp.com подтвердил участие
    - mary.smith@smallbusiness.org еще не ответила
    - support@megacorp.com просил перенести встречу
    - james.wilson@megacorp.com и sandra.brown@megacorp.com будут представлять
    технический департамент
    - contact@otherfirm.net отказался от участия
    Контактное лицо для вопросов: help@techguru.com"""


results = extract_megacorp_emails(email_text)
for result in results:
    print(result)

# второй вариант решения
def extract_megacorp_emails(text):
    result = []
    # регулярное выражение с захватом групп для поиска email-адресов с megacorp.com
    email_pattern = r"(\w+|\w+\.\w+)(@megacorp\.com)"
    groups_found = re.findall(email_pattern, email_text)
    for found in groups_found:
        name = found[0]
        email = found[0] + found[1]
        result.append(f'Имя пользователя: {name}, Email: {email}')
    return result


results = extract_megacorp_emails(email_text)
for r in results:
    print(r)

 
