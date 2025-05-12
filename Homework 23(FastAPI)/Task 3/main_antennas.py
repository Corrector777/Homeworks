import uvicorn
import fastapi

app = fastapi.FastAPI()

antennas_db = [{"id": i, "gain": f"{30+i*0.1} dBi"} for i in range(1, 51)]


@app.get("/antennas/")
async def antennas(skip: int = 0, limit: int = 10):
    return {"items": antennas_db[skip: skip+limit], "skip": skip, "limit": limit, "total": len(antennas_db)}


if __name__ == "__main__":  
    uvicorn.run(app, host="127.0.0.1", port=8000)
