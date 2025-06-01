from pydantic import BaseModel, ValidationError
from fastapi import FastAPI, HTTPException
from typing import Optional, Literal
import uvicorn

app = FastAPI()
app.state.validated_data = {}


class SystemStatusReport(BaseModel):
    system_name: str
    status: Literal["nominal", "warning", "critical", "offline"]
    details: Optional[dict] = None


class SystemSummaryPublic(BaseModel):
    system_id: str
    current_status: str
    critical_reading: Optional[str] = None


@app.post("/titan3/system_status")
async def receive_system_status(system_data: SystemStatusReport):
    """
    Обрабатывает POST-запрос к /titan3/system_status с JSON в следующем формате:
    {
        "system_name": str,
        "status": Literal["nominal", "warning", "critical", "offline"],
        "details": Optional[dict]
    }
    """
    
    app.state.validated_data[system_data.system_name] = system_data
    return {"message": "System data received successfully"}

@app.get("/titan3/system_summary/{system_name}", response_model=SystemSummaryPublic)
async def system_summary_public(system_name: str):
    print(f"Данные в validated_data: {app.state.validated_data}")
    if system_name in app.state.validated_data:
        system_data = app.state.validated_data[system_name]
        current_status = system_data.status
        if system_data.details and system_data.system_name == "Life Support Alpha" and "oxygen_level_percent" in system_data.details:
            critical_reading = f"Oxygen: {system_data.details['oxygen_level_percent']}%"
        else:
            critical_reading = None
        return SystemSummaryPublic(
            system_id=system_name,
            current_status=current_status,
            critical_reading=critical_reading,
        )
    else:
        raise HTTPException(status_code=404, detail="System not found ")
    
if __name__ == "__main__":
    uvicorn.run('task2_post_get:app', host="0.0.0.0", port=8000, reload=True)