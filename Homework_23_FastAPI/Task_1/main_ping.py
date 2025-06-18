from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"status":"online","operator":"Ray"}

@app.get("/ping")
async def ping():
    raise HTTPException(status_code=400, detail="Код станции должен состоять не менее чем из 3 символов")

@app.get("/ping/{station_code}")
async def ping(station_code: str):
    if len(station_code) < 3:
        raise HTTPException(status_code=400, detail="Код станции должен состоять не менее чем из 3 символов")
    return {"station": station_code, "reply": "pong"}

if __name__ == "__main__":  
    uvicorn.run("main_ping:app", host="127.0.0.1", port=8000, reload=True)