
import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

channels_db = [
    {"id": 1, "freq": "145.8", "active": True},
    {"id": 2, "freq": "145.9", "active": False},
    {"id": 3, "freq": "145.10", "active": True},
    {"id": 4, "freq": "145.11", "active": False},
    {"id": 5, "freq": "145.12", "active": True},
    {"id": 6, "freq": "145.13", "active": True},
    {"id": 7, "freq": "145.14", "active": False},
]

@app.get("/channels/{station_code}")
async def channels(station_code: str, active_only: bool = False):
    if active_only:
        channels = [{'id': channel["id"], 'freq': channel["freq"]} for channel in channels_db if channel["active"] is True]
        return {"station": station_code, "channels": channels}
    return {"station": station_code, "channels": [{'id': channel["id"], 'freq': channel["freq"]} for channel in channels_db]}

if __name__ == "__main__":  
    uvicorn.run(app, host="127.0.0.1", port=8000)

