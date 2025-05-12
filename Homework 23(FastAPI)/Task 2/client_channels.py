import requests

exit = {"нет", "no", 'н', 'n'}

while True:

    station_code = input("Введите имя канала: ").lower()
    if len(station_code) < 1:
        print("Ошибка! Ввод не может быть пустым")
        continue
    url = f"http://127.0.0.1:8000/channels/{station_code}"

    channels_status = input("Вывести только активные каналы? (да/нет(=пустой ввод)): ").lower()
    
    match channels_status:
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
    break_point = input('\nПродолжаем(нет/любой ввод = да)?\n')
    if break_point in exit:
        break
    
