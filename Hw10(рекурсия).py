def find_signal(room) -> bool:     # НЕ ЗНАЮ как написать анотацию на 2 возможных типа(строка/лист)
    if room == 'сигнал':
        return True
  
    elif isinstance(room, list):
        for signal in room:          
            find_signal(signal)
        return find_signal(signal)
        
    return False
    

bunker = [
'тишина',
['тишина', ['тишина', ['тишина', 'сигнал'], 'тишина'], 'тишина'],
['тишина', ['тишина', ['тишина', ['тишина']]], 'тишина'],
'тишина'
]

print(find_signal(bunker))             
