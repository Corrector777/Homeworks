from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
from typing import Optional
import uvicorn

app = FastAPI()

mock_titan3_systems_data = {
"Life Support Alpha": {"system_name": "Life Support Alpha", "status":
"critical", "details": {"oxygen_level_percent": 15.5}},
# невалидные данные специально! status = 2, details = [] (2 ошибки валидации)
"Fusion Core Beta": {"system_name": "Fusion Core Beta", "status":2, "details": []}, 
"Hydroponics Bay": {"system_name": "Hydroponics Bay", "status":
"offline", "details": {}},
"Power Plant Gamma": {"system_name": "Power Plant Gamma", "status":
"critical", "details": {"power_consumption_kw": 75.2}},
"Power Plant Delta": {"system_name": "Power Plant Delta", "status":
'offline', "details": {}}
}


class SystemStatusReport(BaseModel):
    system_name: str
    status: str
    details: Optional[dict] = None


class PublicSystemReport(BaseModel):
    system_id: str
    status: str


validated_data: dict[str, SystemStatusReport] = {}
invalid_data: dict[str, list[dict]] = {}
for system in mock_titan3_systems_data:
    system_info = mock_titan3_systems_data[system]
    try:
        system_data = SystemStatusReport(**system_info)
        # print(system_data)
        validated_data[system] = system_data
        # print(validated_data)
    except ValidationError as e:
        # print(f"Ошибка! Невалидные данные: {e.errors()}")
        invalid_data[system] = e.errors()
        print(invalid_data)
        continue


@app.get("/titan3/system_status/{system_id}", response_model=PublicSystemReport)
async def receive_system_status(system_id: str):
    """
    Get the status of a system on Titan-3.

    Args:
    - system_id: The ID of the system to query.

    Returns:
    - A PublicSystemReport containing the system's ID and status.

    Raises:
    - HTTPException 400 if the system ID is invalid or the system is offline.
    - HTTPException 404 if the system ID is not found on Titan-3.
    """

    if system_id in invalid_data:
        errors_list = invalid_data[system_id]
        # создадим список словарей ошибок:
        errors = []
        for error in errors_list:
            errors.append({error['msg']: {'location': error['loc'], 'current_input': error['input'], 'type': error['type']}})
        # print(errors)
        raise HTTPException(status_code=400, detail=errors) 
    if system_id not in validated_data:
        raise HTTPException(status_code=404, detail=f"System with ID \'{system_id}\' not found on Titan-3.") 
    if system_id in validated_data and validated_data[system_id].status == "offline":
        raise HTTPException(status_code=400, detail=f"System with ID \'{system_id}\' is offline and cannot provide data.")
    else:
        response = PublicSystemReport(system_id=system_id, status=validated_data[system_id].status)
        return response


if __name__ == "__main__":
    uvicorn.run('task3:app', host="0.0.0.0", port=8000, reload=True)
