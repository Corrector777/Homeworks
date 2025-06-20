import requests
from requests.exceptions import RequestException
from fastapi import HTTPException
import json
exit = {"нет", "no", 'н', 'n'}

while True:
    station_code = input("Input station code: ")
    try:
        response = requests.get(f"http://127.0.0.1:8000/ping/{station_code}")
        response.raise_for_status()
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    except RequestException as err:
        print(f"Request error: {err}")
        if err.response is not None:
            print(f"Status code: {err.response.status_code}")
            print(f"Response text: {err.response.text}")

    break_point = input('\nПродолжаем(да = любой ввод/нет)?\n')
    if break_point in exit:
        break
