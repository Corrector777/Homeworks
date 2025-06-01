#собирем предыдущиую задачу на методе POST
from pydantic import BaseModel, ValidationError
from fastapi import FastAPI, HTTPException
from typing import Optional, Literal
import uvicorn

app = FastAPI()


class SystemStatusReport(BaseModel):
    system_name: str
    status: Literal["nominal", "warning", "critical", "offline"]
    details: Optional[dict] = None


class SystemSummaryPublic(BaseModel):
    system_id: str
    current_status: Literal["nominal", "warning", "critical", "offline"]
    critical_reading: Optional[str] = None


@app.post("/titan3/system_status", response_model=SystemSummaryPublic)
async def receive_system_status(system_data: SystemStatusReport):
    """
    Обрабатывает POST-запрос к /titan3/system_status с JSON в следующем формате:
    {
        "system_name": str,
        "status": Literal["nominal", "warning", "critical", "offline"],
        "details": Optional[dict]
    }
    Возвращает SystemSummaryPublic объект с system_id, current_status and critical_reading.
    """
    critical_reading = None
    if system_data.details and system_data.details is not None:
        critical_reading = f"Oxygen: {system_data.details['oxygen_level_percent']}%" if system_data.system_name == "Life Support Alpha" and "oxygen_level_percent" in system_data.details else None
    return SystemSummaryPublic(
        system_id=system_data.system_name, 
        current_status=system_data.status, 
        critical_reading=critical_reading)


if __name__ == "__main__":
    uvicorn.run('task2_post:app', host="0.0.0.0", port=8000, reload=True)