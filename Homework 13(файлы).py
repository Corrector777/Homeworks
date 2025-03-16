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
# error_file = None
# errors_list = []

# try:
#     file = open('log.txt', 'r')
#     for line in file:
#         splitted_line = line.split()       
#         if len(splitted_line) >= 3 and splitted_line[2] == 'ERROR':
#             errors_list.append(line)
#     if errors_list:
#         error_file = open('errors.txt', 'w')
#         error_file.writelines(errors_list)
# except FileNotFoundError:
#     print('Ошибка! Файл не найден.')
# except Exception as e:
#     print(f'Найдена ошибка: {e}')
# finally:
#     if file:
#         file.close()
#     if error_file:
#         error_file.close()
# print(f'Найдено ошибок: {len(errors_list)}')

# Задание 3. Составление отчёта из данных нескольких источников
# file1 = None
# file2 = None
# report_list = []

# try:
#     file1 = open('data1.txt', 'r')
#     file2 = open('data2.txt', 'r')
#     for line1 in file1:
#         if line1.stip() and line1 not in report_list:  # if line1.strip()-проверяем, что строка не пустая
#             report_list.append(line1)
#     for line2 in file2:
#         if line2 not in report_list:            
#             report_list.append(line2)
#     if report_list:
#         report_file = open('report.txt', 'w')
#         report_file.writelines(report_list)
#         print("Отчёт успешно сформирован и записан в файл report.txt")
# except FileNotFoundError as e:
#     print(e)
# finally:
#     if file1:
#         file1.close()
#     if file2:
#         file2.close()
#     if report_file:
#         report_file.close()

# Задание 4. Преобразование списка подозреваемых из CSV в простой формат

file = None
new_file = None
suspects_list = []

try:
    file = open('suspects.csv', 'r')
    for line in file:
        splitted_parts = line.strip().split(',')
        new_line = ''.join(splitted_parts[i] + ' - ' for i in range(len(splitted_parts)))
        result_line = new_line[: -3] + '\n'
        suspects_list.append(result_line)
    if suspects_list:
        new_file = open('suspects_out.txt', 'w')
        new_file.writelines(suspects_list)
except FileNotFoundError as e:
    print(e)
finally:
    if file:
        file.close()
    if new_file:
        new_file.close()

print(suspects_list)

