# Задание 1. Расшифровка журнала подсказок

try:
    file = open('clues.log', 'r')
    for line in file:
        if 'подсказка' in line.lower():
            print(line)
except FileNotFoundError:
    print('Ошибка! Файл не найден.')
finally:
    if file:
        file.close()

# Задание 2. Выделение критичных ошибок из журнала событий

