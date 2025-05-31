from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional, Literal
import uvicorn
# Твоя задача, инженер:
# На станции "Звездный Пилигрим" тебе нужно разработать FastAPI эндпоинт /titan3/system_status , который будет принимать POST-запросы с данными о
# состоянии систем станции "Титан-3".
# // Пример данных о состоянии системы жизнеобеспечения
# {
# "system_name": "Life Support Alpha",
# "status": "critical", // может быть "nominal", "warning", "critical",
# "offline"
# "oxygen_level_percent": 15.5,
# "co2_level_ppm": 8000,
# "power_consumption_kw": 75.2,
# "last_maintenance_report_id": "ls-alpha-2042-10-15"
# }
# // Пример данных о состоянии энергоблока
# {
# "system_name": "Fusion Core Beta",
# "status": "warning",
# "output_gw": 0.8,
# "coolant_temp_celsius": 650,
# "active_cells": 3 // из 4
# }
# 1. Создай Pydantic модель SystemStatusReport :
# system_name : строка (str), обязательное поле.
# status : строка (str), обязательное поле. Должно быть одно из следующих
# значений: "nominal", "warning", "critical", "offline". (Пока что для простоты можно не
# реализовывать валидацию на конкретные значения, достаточно типа str , но
# помни об этом ограничении для сюжета).
# details : словарь (dict), необязательное поле. В этом словаре могут приходить
# любые другие параметры, специфичные для системы (например,
# oxygen_level_percent , output_gw и т.д.). Это позволит гибко принимать разные
# типы отчетов.
# 2. Реализуй эндпоинт @app.post("/titan3/system_status") :
# Функция-обработчик должна принимать параметр типа SystemStatusReport .
# Внутри функции просто выведи в консоль полученные данные (например,
# print(f"Received status for {report.system_name}: {report.status}") ).
# В качестве ответа эндпоинт должен возвращать словарь с подтверждением и
# полученными данными, например: {"message": "Status report received
# successfully", "data": report} .
# 3. Проверь работу эндпоинта:
# Используй автоматическую документацию FastAPI ( /docs ) для отправки тестовых
# POST-запросов.
# Попробуй отправить валидные данные для системы жизнеобеспечения и для
# энергоблока (можешь придумать свои поля для словаря details на основе
# примеров выше).
# Попробуй отправить запрос без обязательного поля system_name и посмотри,
# какую ошибку вернет FastAPI (должна быть ошибка 422).
# Попробуй отправить запрос с полем status , но с числовым значением вместо
# строки, и проверь ошибку.

app = FastAPI()


class SystemStatusReport(BaseModel):
    system_name: str
    status: Literal["nominal", "warning", "critical", "offline"]
    details: Optional[dict] = None


@app.post("/titan3/system_status")
async def send_system_status_report(report: SystemStatusReport):
    '''Функция обработки данных о состоянии системы. Принимает словарь с данными о состоянии 
    системы и возвращает словарь с сообщением об успешном получении данных'''

    print(f"Received status for {report.system_name}: {report.status}")
    return {"message": "Status report received successfully", "data": report}

if __name__ == "__main__":
    uvicorn.run("task1:app", host="127.0.0.1", port=8000, reload=True)
