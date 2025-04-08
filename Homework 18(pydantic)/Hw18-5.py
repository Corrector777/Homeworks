# task_5_serialization.py
from pydantic import BaseModel, Field, ValidationError  # Не забудь Field
import pprint  # Для красивого вывода словаря


# --- Данные для лога юнита Анубис ---
log_data = {
    "unit_id": "ANU-01-ISIS",
    "status": "Scanning Sector-Zeta",
    "location": "Inner Chamber Coordinates [11.3, -25.7, 8.0]",
    "calibration_key": "AX7-j#pL$q9@zRtY"  # Этот ключ не должен попасть в лог
    }


# --- Модели ---
# ТВОЙ КОД ЗДЕСЬ: Определи класс AnubisUnitLog
# - unit_id: str
# - status: str
# - location: str
# - calibration_key: str, используй Field(..., exclude=True) для исключения при сериализации
class AnubisUnitLog(BaseModel):
    unit_id: str
    status: str
    location: str
    calibration_key: str = Field(exclude=True)


# --- Логика скрипта ---
print("--- Задание 5: Экспорт Данных для Лога ---")
# AnubisUnitLog = None # Заглушка
# ВАЖНО: Когда ты определишь класс AnubisUnitLog выше, удали или закомментируй эту строку
anubis_log = None  # Инициализация
log_dict = None
log_json = None
if AnubisUnitLog is not None:
    try:
        # ТВОЙ КОД ЗДЕСЬ: Создай экземпляр anubis_log из log_data
        anubis_log = AnubisUnitLog(**log_data)  # Замени None
        if anubis_log:
            print(f"Объект лога для {anubis_log.unit_id} создан.")
            # Внутри объекта ключ существует:
            print(f"(Внутренний ключ: {anubis_log.calibration_key})")  #Убедимся, что он там есть
            print("\n1. Сериализация в словарь (.model_dump()):")
            # ТВОЙ КОД ЗДЕСЬ: Получи словарь из anubis_log с помощью model_dump()
            log_dict = anubis_log.model_dump() # Замени None на вызов метода
            pprint.pprint(log_dict if log_dict else "Словарь не был создан.")
    
            print("\n2. Сериализация в JSON (.model_dump_json()):")
            # ТВОЙ КОД ЗДЕСЬ: Получи JSON-строку из anubis_log с помощью model_dump_json(indent=2)
            log_json = anubis_log.model_dump_json(indent=2) # Замени None на вызов метода
            print(log_json if log_json else "JSON не был создан.")
            # Проверка (необязательно, но полезно): убедимся, что ключа нет в выводе
            key_in_dict = 'calibration_key' in log_dict if isinstance(log_dict, dict) else False
            key_in_json = '"calibration_key"' in log_json if isinstance(log_json, str) else False
            print(f"\nКлюч 'calibration_key' присутствует в словаре?\
{key_in_dict}")
            print(f"Ключ 'calibration_key' присутствует в JSON?\
{key_in_json}")
        else:
            print("Экземпляр anubis_log не был создан.")
    except ValidationError as e:
        print(f"Ошибка валидации при создании объекта лога:\n{e}")
    except Exception as e:
        print(f"Произошла другая ошибка: {e}")
else:
    print("Класс AnubisUnitLog еще не определен.")
    print("-" * 40)


# Ожидаемый результат (после того, как ты напишешь код):
# --- Задание 5: Экспорт Данных для Лога ---
# Объект лога для ANU-01-ISIS создан.
# (Внутренний ключ: AX7-j#pL$q9@zRtY)

# 1. Сериализация в словарь (.model_dump()):
# {'location': 'Inner Chamber Coordinates [11.3, -25.7, 8.0]',
# 'status': 'Scanning Sector-Zeta',
# 'unit_id': 'ANU-01-ISIS'}

# 2. Сериализация в JSON (.model_dump_json()):
# {
# "unit_id": "ANU-01-ISIS",
# "status": "Scanning Sector-Zeta",
# "location": "Inner Chamber Coordinates [11.3, -25.7, 8.0]"
# }
# Ключ 'calibration_key' присутствует в словаре? False
# Ключ 'calibration_key' присутствует в JSON? False