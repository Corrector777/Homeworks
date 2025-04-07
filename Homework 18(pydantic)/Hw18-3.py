# task_3_nested_lists.py
from pydantic import BaseModel, ValidationError
from typing import List, Optional # Не забудь импортировать List

# --- Данные о тяжелом юните ---
sekhmet_data = {
    "unit_id": "SKH-01-PRIME",
    "callsign": "Разрушитель",
    "equipment": [
        {"name": "Плазменный резак", "condition": 0.95},
        {"name": "Силовой щит 'Эгида'", "condition": 0.81},
        {"name": "Ремкомплект Мк.3", "condition": 1.0}
        ]
}


# --- Модели ---
# ТВОЙ КОД ЗДЕСЬ: Определи класс EquipmentItem
# - name: str
# - condition: float
class EquipmentItem(BaseModel):
    name: str
    condition: float


# ТВОЙ КОД ЗДЕСЬ: Определи класс SekhmetUnit
# - unit_id: str
# - callsign: str
# - equipment: список объектов EquipmentItem (List[EquipmentItem])
class SekhmetUnit(BaseModel):
    unit_id: str
    callsign: str
    equipment: List[EquipmentItem]


# --- Логика скрипта ---
print("--- Задание 3: Инвентарь Тяжелого Юнита ---")
# SekhmetUnit = None # Заглушка
# EquipmentItem = None # Заглушка
# ВАЖНО: Когда ты определишь классы EquipmentItem и SekhmetUnit выше, удали или закомментируй эти строки
# sekhmet_unit = None # Инициализация
try:
    # Проверяем, что классы определены перед использованием
    if EquipmentItem is not None and SekhmetUnit is not None:
        # ТВОЙ КОД ЗДЕСЬ: Создай экземпляр sekhmet_unit из sekhmet_data
        sekhmet_unit = SekhmetUnit(**sekhmet_data)  # Замени None
    else:
        print("Классы EquipmentItem и/или SekhmetUnit еще не определены.")
    if sekhmet_unit:
        print(f"Юнит '{sekhmet_unit.callsign}' (ID: {sekhmet_unit.unit_id}) успешно загружен.")
        print("Инвентарь:")
        # ТВОЙ КОД ЗДЕСЬ: Пройдись циклом по sekhmet_unit.equipment и выведи имя каждого предмета (item.name) и состояние (item.condition)
        # Используй `if sekhmet_unit.equipment:` для проверки, что список не пуст
        if sekhmet_unit.equipment:
            for item in sekhmet_unit.equipment:
                print(f'- {item.name} (Состояние: {item.condition})')
        else:
            print("Инвентарь пуст (или не удалось получить доступ).")
    elif EquipmentItem is not None and SekhmetUnit is not None:
        print("Экземпляр SekhmetUnit не был создан.")
except ValidationError as e:
    print(f"Ошибка валидации при создании объекта SekhmetUnit:\n{e}")
except NameError:
    print("Один из классов (EquipmentItem или SekhmetUnit) еще не определен!")
except Exception as e:
    print(f"Произошла другая ошибка: {e}")
    print("-" * 40)

# Ожидаемый результат (после того, как ты напишешь код):
# --- Задание 3: Инвентарь Тяжелого Юнита ---
# Юнит 'Разрушитель' (ID: SKH-01-PRIME) успешно загружен.
# Инвентарь:
# - Плазменный резак (Состояние: 0.95)
# - Силовой щит 'Эгида' (Состояние: 0.81)
# - Ремкомплект Мк.3 (Состояние: 1.0)
# ----------------------------------------