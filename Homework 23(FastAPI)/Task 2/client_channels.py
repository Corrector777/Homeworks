import requests

exit = {"exit", "Exit", 'x', 'ч'}

while True:

    station_code = input("Введите имя канала: ").lower()
    url = "http://127.0.0.1:8000/channels/{station_code}"
    if station_code in exit:
        print("До скорых встреч")
        break

    channel_name = input("Вывести только активные каналы? (да/нет): ").lower()
    match channel_name:
        case 'да':
            print("\nАктивные каналы")
            response = requests.get(url, params={"active_only": True})
            print(response.json())
        case 'нет' | '':
            print("\nВсе каналы")
            response = requests.get(url, params={"active_only": False})
            print(response.json())
        case _:
            print("Некорректный ввод")
    print('\nПродолжаем\n')
    
