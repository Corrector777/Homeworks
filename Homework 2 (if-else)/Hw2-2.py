#### Задание 2: Расшифровка кода доступа  
# Условие:  
# Даны четыре булевы переменные:  
# python  

 
# Код доступа активируется, если выполняется только одно из условий:  
# 1. (A and 😎 or (C and D)  
# 2. (A != D) and (B == C)  
# 3. not (A or C) and (B or D)  

# Напишите код, который определяет, активирован ли код, и выводит номер условия, которое было выполнено. Если ни одно не выполнено или выполнено несколько — вывести "Отказ".  

A = False
B = False
C = True
D = False 
cond1 = A and B or (C and D)  
cond2 = (A != D) and (B == C)   
cond3 = not (A or C) and (B or D)           

count = cond1 + cond2 + cond3
# print(count)
if count == 1:
    if A and B or (C and D):
        print('условие 1')
    elif (A != D) and (B == C):     # Вот тут во входных данных может быть засада!!!!
        print('условие 2')
    elif not (A or C) and (B or D):
        print('условие 3')
else:
    print('отказ')

