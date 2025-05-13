from fastapi import FastAPI
import requests
from requests.exceptions import RequestException

# запросы к сервисам
url_1 = "http://127.0.0.1:8000/ping/Vega-11"
url_2 = "http://127.0.0.1:8001/channels/Vega-11"
params_2 = {
    "active_only": True
}
url_3 = "http://127.0.0.1:8002/antennas"
params_3 = {
    "skip": 0,
    "limit": 1000
}

#FastAPI report
app = FastAPI()


@app.get("/report")
async def report():
    pong = None
    channels = None
    antennas_total = None
    if params_2["active_only"]:
        channels_status = "active_channels"
    else:
        channels_status = "all_channels"
    try:
        response_1 = requests.get(url_1)
        response_1.raise_for_status()
        pong = response_1.json()["reply"]
        response_2 = requests.get(url_2, params=params_2)
        response_2.raise_for_status()
        channels = len(response_2.json()["channels"])
        response_3 = requests.get(url_3, params=params_3)    
        response_3.raise_for_status()    
        antennas_total = len(response_3.json()["items"])
    except RequestException as err:
        print(f"Request error: {err}")
        return {
                'error': 'Внимание, не все запросы выполнены!',
                'details': str(err),
                'data': {
                    'pong': pong,
                    channels_status: channels,
                    'antennas_total': antennas_total
                    }
                }
                
    print(f'Данные для отчета: \n"pong": {pong}, {channels_status}: {channels}, "antennas_total": {antennas_total}')
    return {
            'pong': pong,
            channels_status: channels,
            'antennas_total': antennas_total
            }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8003)

