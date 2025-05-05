import requests

exit = {"exit", "Exit", 'x', 'ч'}

while True:
    station_code = input("Input station code: ")
    if station_code in exit:
        break
    response = requests.get(f"http://127.0.0.1:8000/ping/{station_code}")
    print(response.json())
