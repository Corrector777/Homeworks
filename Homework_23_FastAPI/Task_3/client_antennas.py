import requests
from requests.exceptions import RequestException

antennas_list: list[dict] = []
current_skip = 0
current_limit = 10
while True:
    url = "http://127.0.0.1:8002/antennas/"
    params = {
        "skip": current_skip,
        "limit": current_limit
    }
    try:
        response = requests.get(url, params=params)
        total = response.json()["total"]
        items = response.json()["items"]
        if len(antennas_list) < total:
            response.raise_for_status()
            antennas_list += items
            print(f'{len(items)} антенн от {current_skip + 1} до {current_skip + len(items)} добавлены:')
            print(response.json(), "\n")
            current_skip += len(items)
        else:
            break
    except RequestException as err:
        print(f"Request error: {err}")
        if err.response is not None:
            print(f"Status code: {err.response.status_code}")
            print(f"Response text: {err.response.text}")
            break

print(f'всего получено антенн: {len(antennas_list)}')

