from fastapi import FastAPI, HTTPException  
from pydantic import BaseModel, ValidationError
from typing import Optional, Literal, List
import random
import uvicorn
import uuid  

app = FastAPI()


class EvacuationRequestDetails(BaseModel):
    requesting_ship_name: str
    priority_level: int
    personnel_to_evacuate: int
    additional_notes: Optional[str] = None


class EvacuationPlanResponse(BaseModel):
    titan_station_id: str = 'Titan-3'
    plan_id: str
    rendezvous_point_coordinates: str
    estimated_time_to_prepare_sec: int
    critical_resource_needs: Optional[List[str]] = None


@app.post("/titan3/request_evacuation_plan", response_model=EvacuationPlanResponse)
async def request_evacuation_plan(request_details: EvacuationRequestDetails):
    if request_details.personnel_to_evacuate > 50:
        print("[WARNING!] Titan-3 cannot currently prepare evacuation for more than 50 personnel due to system limitations.")
        raise HTTPException(status_code=400, detail="Titan-3 cannot currently prepare evacuation for more than 50 personnel due to system limitations.")
    elif request_details.personnel_to_evacuate <=0:
        print("[WARNING!] Invalid number of personnel to evacuate.")
        raise HTTPException(status_code=400, detail="Invalid number of personnel to evacuate.")
    else:
        plan_id = f"EVAC-PLAN-{uuid.uuid4().hex[:8].upper()}"
    point_coordinates = random.choice(["Сектор Гамма-7", "Точка Лагранжа L2", "Пояс Ореона"])
    estimated_time_to_prepare_sec = random.randint(300, 600)
    critical_resource_needs = [random.choice(["Дополнительные кислородные баллоны", "Ремонтный комплект для шлюза B", "Бортовой журнал"])]
    if request_details.personnel_to_evacuate > 20:
        print("[WARNING!] Для эвакуации более 20 человек требуется шаттл повышенной вместимости.")
        critical_resource_needs.append("Транспортный шаттл повышенной вместимости")
    # Ваш код для обработки запроса
    return EvacuationPlanResponse(
        titan_station_id='Titan-3',
        plan_id=plan_id,
        rendezvous_point_coordinates=point_coordinates,
        estimated_time_to_prepare_sec=estimated_time_to_prepare_sec,
        critical_resource_needs=critical_resource_needs
        )

if __name__ == "__main__":
    uvicorn.run('task4:app', host="0.0.0.0", port=8000, reload=True)