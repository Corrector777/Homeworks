import random

items = ['меч', 'щит', 'зелье', 'ключ']
riddles = ['Острое и блестящее', 'Защитит от удара', 'Восстанавливает силы',
'Открывает любые двери']


# my_dict = {key: value for key in items for value in riddles}


def my_first_iterator():
    for _ in range(len(items)):
        index = random.choice(range(len(items)))
        yield (items[index], riddles[index])
    yield "Сундук пуст, поиск окончен!"

iterator = iter(my_first_iterator())

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

