import requests
from requests.exceptions import RequestException

details = input("Показать детали(да = любой ввод/нет)?\n")
if details in {"нет", "no", 'н', 'n'}:
    url = "http://127.0.0.1:8003/report"
else:
    url = "http://127.0.0.1:8003/report?details=True"
#запрос к FastAPI report
try:
    response_4 = requests.get(url)
    response_4.raise_for_status()
    print(response_4.json())
except RequestException as err:
    print(f"Request error: {err}")
    if err.response is not None:
        print(f"Status code: {err.response.status_code}")
        print(f"Response text: {err.response.text}")