def echo(message: str, count: int) -> print:
    '''Функция ЭХО. 
    ARGS:сообщение(строка), кол-во повторений(int)
    Вывод: выводит на печать сообщение заданное 
    кол-во раз в пронумерованном порядке'''
    if (isinstance(count, int) and isinstance(message, str)):
        if count <= 0:
            pass
        elif count > 0:        
            echo(message, count - 1)
            print(f'Echo {count}: {message}')
    else:
        print("Ошибка! Проверь корректность ввода(типы аргументов)")


# message = "Help me!"
# count = 3
# echo(message, count)

# Задание 2


def thread(length: int) -> print:
    '''Функция выводит размер каждой петли нити
        от заданной длины до 1
        ARG: длина(int)
        Вывод: размер каждой петли нити
        от заданной длины до 1 '''
    if isinstance(length, int):
        if length <= 0:
            pass
        elif length > 0:
            print(f'Thread loop of size: {length}')
            thread(length - 1)
    else:
        print("Ошибка! введенное значение не является числом")


# length = 5
# thread(length)


# Задание 3: «Следы Минотавра»

def minotaur_steps(tracks: int):
    '''Функция считает и возвращает общее количество шагов
      Минотавра по числу следов.
      ARG: число следов (int)
      Возвращает кол-во шагов''' # а именно самый первый вызов 
      #рекурсивной функции minotaur_steps(tracks). Сначала функция рекурсивно вызывает
      #  сама себя до тех пор, пока tracks не будет равен 0.Затем в обратном порядке возвращает из стека значения
      #всех вызванных собой же функций и возвращает их значения по очереди.Последнее вернувшееся значение из стека вызовов(первая вызванная рекурсивная функция)
      #  и есть наше искомое кол-во шагов
    if isinstance(tracks, int):
        if tracks <= 0:
            pass
        elif tracks > 0:
            minotaur_steps(tracks - 1)
            return f'Total steps: {tracks}'
    return "Ошибка! введенное значение не является числом"


tracks = 4   
print(minotaur_steps(tracks))