from pydantic import BaseModel, ValidationError
from typing import Optional
# Ваша задача: Определить модель UnitStatus со следующими полями:
# unit_id : строка, обязательное поле.
# energy_level : целое число, обязательное поле.
# last_patrol_zone : строка, опциональное поле (может быть None ). Значение по умолчанию должно быть None .
# operational_mode : строка, необязательное поле со значением по умолчанию = "Patrol" .

# Создать два экземпляра: один со всеми переданными полями, другой - только с
# обязательными. Вывести результат .model_dump() для обоих экземпляров.
# --- Данные отчетов от юнитов ---
status_data_full = {
    "unit_id": "SKH-03-GAMMA",
    "energy_level": 88,
    "last_patrol_zone": "Sector-Gamma-3",
    "operational_mode": "Standby" # Переопределяем дефолт
    }
status_data_minimal = {
    "unit_id": "SPX-11-DELTA",
    "energy_level": 95
# last_patrol_zone и operational_mode не переданы
}
# --- Модели ---
# ТВОЙ КОД ЗДЕСЬ: Определи класс UnitStatus
# - unit_id: str (обязательное)
# - energy_level: int (обязательное)
# - last_patrol_zone: Optional[str], значение по умолчанию None
# - operational_mode: str, значение по умолчанию "Patrol"
class UnitStatus(BaseModel):
    unit_id: str
    energy_level: int
    last_patrol_zone: Optional[str] = None
    operational_mode: str = "Patrol"

# --- Логика скрипта ---
print("--- Задание 2: Статус Оперативности ---")
# UnitStatus = None # Заглушка, чтобы код ниже не падал сразу
# ВАЖНО: Когда ты определишь класс UnitStatus выше, удали или закомментируй эту строку
if UnitStatus is not None: # Проверяем, определен ли класс
    try:
    # ТВОЙ КОД ЗДЕСЬ: Создай экземпляр status_1 из status_data_full
        status_1 = UnitStatus(**status_data_full)  # Замени None
        print("Статус 1 (Полные данные):")
    # ТВОЙ КОД ЗДЕСЬ: Выведи результат model_dump() для status_1
        print(status_1.model_dump() if status_1 else "Экземпляр status_1 не создан")
    except ValidationError as e:
        print(f"Ошибка при создании status_1:\n{e}")
    except Exception as e:
        print(f"Другая ошибка при обработке status_1: {e}")
    print("-" * 20)
    try:
    # ТВОЙ КОД ЗДЕСЬ: Создай экземпляр status_2 из status_data_minimal
        status_2 = UnitStatus(**status_data_minimal) # Замени None
        print("Статус 2 (Минимальные данные):")
    # ТВОЙ КОД ЗДЕСЬ: Выведи результат model_dump() для status_2
        print(status_2.model_dump() if status_2 else "Экземпляр status_2 не создан")
    except ValidationError as e:
        print(f"Ошибка при создании status_2:\n{e}")
    except Exception as e:
        print(f"Другая ошибка при обработке status_2: {e}")
else:
    print("Класс UnitStatus еще не определен. Сначала определи его!")

print("-" * 40)

# Ожидаемый результат (после того, как ты напишешь код):
# --- Задание 2: Статус Оперативности ---
# Статус 1 (Полные данные):
# {'unit_id': 'SKH-03-GAMMA', 'energy_level': 88, 'last_patrol_zone': 'Sector-
# Gamma-3', 'operational_mode': 'Standby'}
# --------------------
# Статус 2 (Минимальные данные):
# {'unit_id': 'SPX-11-DELTA', 'energy_level': 95, 'last_patrol_zone': None,
# 'operational_mode': 'Patrol'}
# ----------------------------------------

