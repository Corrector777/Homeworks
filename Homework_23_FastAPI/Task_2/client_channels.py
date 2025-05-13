import requests
from requests.exceptions import RequestException

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
            try:
                print("\nАктивные каналы")
                response = requests.get(url, params={"active_only": True})
                response.raise_for_status()
                print(response.json())
            except RequestException as err:
                print(f"Request error: {err}")
                if err.response is not None:
                    print(f"Status code: {err.response.status_code}")
                    print(f"Response text: {err.response.text}")
        case 'нет' | '':
            try:
                print("\nВсе каналы")
                response = requests.get(url, params={"active_only": False})
                response.raise_for_status()
                print(response.json())
            except RequestException as err:
                print(f"Request error: {err}")
                if err.response is not None:
                    print(f"Status code: {err.response.status_code}")
                    print(f"Response text: {err.response.text}")
        case _:
            print("Некорректный ввод")
    break_point = input('\nПродолжаем(нет/любой ввод = да)?\n')
    if break_point in exit:
        break
    
