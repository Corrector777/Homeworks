# #### Задание 5: Оптимизация тернарным оператором  
# Условие:  
# Дана переменная:  
# score = -5
  
# Напишите один тернарный оператор, который преобразует score в оценку по правилам:  
# - 90-100 → "A"  
# - 80-89 → "B"  
# - 70-79 → "C"  
# - 60-69 → "D"  
# - 0-59 → "F"  
# - Если score не в диапазоне 0-100 → "Ошибка".  

# Ограничение: Нельзя использовать if-elif-else, только тернарные операторы.
question_flag = True
while True:
    count_flag = True 
    if question_flag:
        try:
            score = int(input('Enter your count: '))
        except ValueError:
            print('Только числа')
            count_flag = False
        if count_flag:
            print('A' if 100 >= score >= 90 else 'B' if 89 >= score >= 80 else 'C' if 79 >= score >= 70 else "D" if 69 >= score >= 60 else 'F' if 59 >= score >= 0 else 'Ошибка')
            question = input('продолжим(да/нет)?: ')
            question_flag = False

    elif question.lower() == 'да':
        question_flag = True    
    elif question.lower() == 'нет':
        print('До скорых встреч')
        break         
    else:
        question_flag = False
        print('некорректный ответ')
        question = input('продолжим(да/нет)?: ')

