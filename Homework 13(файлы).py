# Задание 1. Расшифровка журнала подсказок
# file = None  # избегаем ошибки NameError: name 'file' is not defined в блоке finally(если файла нет) 
# try:
#     file = open('clues.log', 'r')
#     for line in file:
#         if 'подсказка' in line.lower():
#             print(line.strip())
# except FileNotFoundError:
#     print('Ошибка! Файл не найден.')
# finally:
#     if file:
#         file.close()

# Задание 2. Выделение критичных ошибок из журнала событий
# file = None
# errors_list = []

# try:
#     file = open('log.txt', 'r')
#     for line in file:
#         if 'ERROR' in line:
#             errors_list.append(line)
#     if errors_list:
#         error_file = open('errors.txt', 'w')
#         error_file.writelines(errors_list)
# except FileNotFoundError:
#     print('Ошибка! Файл не найден.')
# finally:
#     if file:
#         file.close()
#     if error_file:
#         error_file.close()