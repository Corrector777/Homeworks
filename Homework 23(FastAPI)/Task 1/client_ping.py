import requests

exit = {"нет", "no", 'н', 'n'}

while True:
    station_code = input("Input station code: ").lower()
    response = requests.get(f"http://127.0.0.1:8000/ping/{station_code}")
    print(response.json())
    break_point = input('\nПродолжаем(да = любой ввод/нет)?\n')
    if break_point in exit:
        break
