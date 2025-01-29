import random


count = 1
random_number = random.randint(1, 100)
while True:
    try:
        my_number = int(input("Введите число: "))       
        if my_number > random_number:
            count += 1
            print('Ваше число больше')
        elif my_number < random_number:
            count += 1
            print('Ваше число меньше сгенерированного')
        else:
            print(f'Верно! Ваше число = {my_number}. Вы угадали его с {count}й попытки')
            break
    except ValueError:
        print('Ай-яй!! Принимаю только численные значения')