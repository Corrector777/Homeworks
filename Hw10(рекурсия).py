def find_signal(room) -> bool:     # НЕ ЗНАЮ как написать анотацию на 2 возможных типа(строка/лист)
    if room == 'сигнал':
        return True
    if room == 'тишина':
        return False
  
    if isinstance(room, list):
        for signal in room:          
            find_signal(signal)
        return find_signal(signal)
        
    # else:
    #     print('Error')
    

bunker = [
'тишина',
['тишина', ['тишина', ['тишина', 'сигнал'], 'тишина'], 'тишина'],
['тишина', ['тишина', ['тишина', ['тишина']]], 'тишина'],
'тишина'
]

print(find_signal(bunker))             
