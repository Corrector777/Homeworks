#### Задание 1: Валидация транзакции  
# Условие:  
# Напишите код, который проверяет корректность банковской транзакции по следующим правилам:  
# 1. Сумма (`amount`) должна быть положительной и не превышать 100000.  
# 2. Тип операции (`operation_type`) может быть только "перевод" или "оплата".  
# 3. Для операций "перевод" комиссия (`fee`) не должна превышать 5% от суммы.  
# 4. Если операция "оплата", сумма должна быть кратна 100.  
# Вывод:  
# - Если все условия выполнены: "Транзакция разрешена".  
# - Если хотя бы одно нарушено: "Ошибка: [описание проблемы]" (указать первую обнаруженную ошибку в порядке проверки).  


amount = 90000
operation_type = 'перевод'  
fee = 700  
  
if 0 >= amount or amount > 100000:
    print('Ошибка: недопустимая сумма')

elif operation_type.lower() not in ['перевод', 'оплата']:
    print('Ошибка: неверный тип операции')

elif operation_type == 'перевод' and fee > (amount / 100 * 5):
    print('Ошибка: комиссия превышает 5%')

elif operation_type == 'оплата' and (amount % 100) != 0:
    print('Ошибка: не кратно 100')

else:
    print('транзакция разрешена')


if operation_type.lower() == 'перевод' or 'оплата':     # проверка на тип операции
    if 0 >= amount or amount > 100000:      # проверка на значение суммы
        print('Ошибка: недопустимая сумма')
    elif operation_type == 'перевод' and fee > (amount / 100 * 5):      # проверка комиссии перевода
        print('Ошибка: комиссия превышает 5%')
    elif operation_type == 'оплата' and (amount % 100) != 0:     # роверка кратности 100 суммы оплаты
        print('Ошибка: не кратно 100')
    else:
        print('транзакция разрешена')   # если ни одно условие из внутренних циклов не сработало, то операция разрешена
else:
    print('Ошибка: неверный тип операции')   # если первое условие ложно, то тип данных не знаком
