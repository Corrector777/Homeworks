import requests
from requests.exceptions import RequestException


#запрос к FastAPI report
try:
    response_4 = requests.get("http://127.0.0.1:8003/report")
    response_4.raise_for_status()
    print(response_4.json())
except RequestException as err:
    print(f"Request error: {err}")
    if err.response is not None:
        print(f"Status code: {err.response.status_code}")
        print(f"Response text: {err.response.text}")