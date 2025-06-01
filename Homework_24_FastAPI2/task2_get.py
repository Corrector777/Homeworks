from pydantic import BaseModel, ValidationError
from fastapi import FastAPI, HTTPException
from typing import Optional, Literal
import uvicorn

# Твоя задача, инженер:
# Модифицируй свой FastAPI эндпоинт (или создай новый, если удобнее, например,
# /titan3/system_summary/{system_name} ), чтобы он не просто принимал данные, а
# возвращал краткую сводку для бортового журнала "Звездного Пилигрима", используя
# response_model .
# 1. Создай Pydantic модель SystemSummaryPublic для ответа:
# system_id : строка (str). Это будет system_name из входящего запроса.
# current_status : ст#рока (str). Это будет status из входящего запроса.
# critical_reading : строка (str), необязательное поле ( Optional[str] = None ).
# Сюда мы будем записывать значение, например, уровня кислорода, если система
# – "Life Support Alpha" и такое поле есть в details . Для других систем или если
# данных нет, это поле будет None .
# 2. Обнови свой эндпоинт (или создай новый GET эндпоинт, который будет брать
# данные из некоего внутреннего хранилища, куда ты их "сохранил" в Задании 1):
# Укажи response_model=SystemSummaryPublic в декораторе эндпоинта.
# Функция-обработчик должна:
# Принять данные о системе ( Betлибо как в Задании 1 через POST, либо, если
# делаешь GET, представь, что ты извлекаешь ранее сохраненный
# SystemStatusReport по имени системы).
# Сформировать словарь или объект SystemSummaryPublic на основе
# полученных данных.
# Для поля critical_reading : если system_name это "Life Support Alpha" и в
# details есть ключ oxygen_level_percent , то значение critical_reading
# должно быть строкой вида "Oxygen: X%" , где X – значение уровня
# кислорода. В остальных случаях critical_reading остается None .
# Вернуть этот сформированный объект/словарь. FastAPI, благодаря
# response_model , отфильтрует все лишнее и приведет типы.
# 3. Проверь работу эндпоинта:
# Используй /docs .
# Отправь данные (или запроси их), где system_name – "Life Support Alpha" и в
# details есть oxygen_level_percent . Убедись, что в ответе есть поле
# critical_reading с корректным значением.
# Отправь данные для другой системы (например, "Fusion Core Beta"). Убедись, что
# в ответе поле critical_reading отсутствует или равно null (в зависимости от
# того, как FastAPI сериализует None для необязательных полей, если они не
# предоставлены).
# Убедись, что в ответе нет никаких других полей из SystemStatusReport.details
# или других полей, не описанных в SystemSummaryPublic .
# Алекс: "Так-то лучше! Теперь капитан будет получать только ту информацию, которая ей
# действительно нужна, и в предсказуемом формате. Никаких больше сюрпризов от API
# "Титан-3" в наших отчетах!"

app = FastAPI()

data = [
    {
        "system_name": "Life Support Alpha",
        "status": "critical",
        "details": {
            "oxygen_level_percent": 15.5,
            "co2_level_ppm": 8000,
            "power_consumption_kw": 75.2,
            "last_maintenance_report_id": "ls-alpha-2042-10-15"
        }
    },
    {
        "system_name": "Fusion Core Beta",
        "status": "warning",
        "details": {
            "output_gw": 0.8,
            "coolant_temp_celsius": 650,
            "active_cells": 3
        }
    },
    {
        "system_name": "Fusion Core Gamma",
        "status": "unknown",
        "details": {
            "output_gw": 0.9,
            "coolant_temp_celsius": 850,
            "active_cells": 4
        }   
    }
]


class SystemStatusReport(BaseModel):
    system_name: str
    status: Literal["nominal", "warning", "critical", "offline"]
    details: Optional[dict] = None


class SystemSummaryPublic(BaseModel):
    system_id: str
    current_status: str
    critical_reading: Optional[str] = None


# валидация данных data
validated_data: dict[str, SystemStatusReport] = {}
for system in data:
    try:
        system_report = SystemStatusReport(**system)
        validated_data[system["system_name"]] = system_report
    except ValidationError as e:
        # невалидные данные(статус не валиден) не будут являться объектом SystemStatusReport(поэтому ниже в проверке будет ошибка
        # с указанием невалидного статуса - для гибкости)
        validated_data[system["system_name"]] = {'non_valid_data': system, 'errors': e.errors()}

# print(system['system_name'])
# print(system_report)
print(validated_data)
    

@app.get("/titan3/system_summary/{system_name}", response_model=SystemSummaryPublic)
async def system_summary_public(system_name: str):
    '''Эта функция использует словарь validated_data(Pydantic модель) для поиска данных системы, соответствующих указанному system_name.
      Она возвращает объект SystemSummaryPublic,
      который включает system_id, current_status и, при необходимости, critical_reading для систем "Life Support Alpha".'''
    print('Проверка', system_name)
    if system_name in validated_data:
        system_data = validated_data[system_name]
        # если system_data является объектом Pydantic модели SystemStatusReport(имеет аттрибут), 
        # то извлекаем его аттрибуты     
        if hasattr(system_data, 'status'):
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
        # Если system_data не является объектом Pydantic модели SystemStatusReport, а является словарем с невалидными данными,
        # то возвращаем ошибку с указанием невалидного статуса
        else:
            raise HTTPException(status_code=400, detail="Status must be one of ['nominal', 'warning', 'critical', 'offline']")
    else:
        raise HTTPException(status_code=404, detail="System not found ")

if __name__ == "__main__":
    uvicorn.run("task2_get:app", host="127.0.0.1", port=8000, reload=True)
