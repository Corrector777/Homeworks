from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"status":"online","operator":"Ray"}

@app.get("/ping/{station_code}")
async def ping(station_code: str):
    if not station_code or len(station_code) < 3:
        raise HTTPException(status_code=400, detail="Код станции должен состоять не менее чем из 3 символов")
    return {"station": station_code, "reply": "pong"}

if __name__ == "__main__":  
    uvicorn.run(app, host="127.0.0.1", port=8000)