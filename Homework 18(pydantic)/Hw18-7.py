from pydantic import BaseModel, Field, ConfigDict, ValidationError
from typing import Annotated # Для удобного использования Field с типами
import json
import pprint # Для красивого вывода


# --- Данные от устаревшей системы (camelCase) ---
legacy_data = {
        "guardianId": "PROTO-G-001",
        "currentTask": "Observe Entrance C",
        "isActiveStatus": True
    }

# print("словарь", legacy_data)
# legacy_data_json = json.dumps(legacy_data) # Преобразуем в JSON()
# print("Json", legacy_data_json)


# --- Модель данных ---
# ТВОЙ КОД ЗДЕСЬ: Определи класс LegacyGuardianData
# - guardian_id: str, алиас 'guardianId'
# - current_task: str, алиас 'currentTask'
# - is_active_status: bool, алиас 'isActiveStatus'
# - Добавь model_config = ConfigDict(populate_by_name=True)
class LegacyGuardianData(BaseModel):
# # Используем Annotated для чистоты
    guardian_id: Annotated[str, Field(alias='guardianId')]
    current_task: Annotated[str, Field(alias='currentTask')]
    is_active_status: Annotated[bool, Field(alias='isActiveStatus')]
    model_config = ConfigDict(populate_by_name=True)


# --- Логика скрипта ---
print("--- Задание 7: Интеграция с Устаревшей Системой ---")
# LegacyGuardianData = None  # Заглушка
# ВАЖНО: Когда ты определишь класс LegacyGuardianData выше, удали или закомментируй эту строку
guardian_instance = None  # Инициализация
dumped_with_alias = None
dumped_without_alias = None
if LegacyGuardianData:
    try:
        # ТВОЙ КОД ЗДЕСЬ: Создай экземпляр guardian_instance из legacy_data
        # Используй метод класса model_validate() - он учтет алиасы при работе со словарем
        # guardian_instance = LegacyGuardianData(guardian_id='Test', current_task='Test', is_active_status=False)  #Используем populate_by_name=True
        guardian_instance = LegacyGuardianData.model_validate(legacy_data)  # Замени None
        if guardian_instance:            
            print("Объект успешно создан из данных с camelCase ключами.")
            # Доступ к данным через Python-имена
            print(f"ID Стража (Python): {guardian_instance.guardian_id}")
            print(f"Текущая задача (Python): {guardian_instance.current_task}")
            print(f"Статус (Python): {guardian_instance.is_active_status}")
            print("\nВыгрузка данных с использованием алиасов (by_alias=True):")
            # ТВОЙ КОД ЗДЕСЬ: Получи словарь из guardian_instance с опцией by_alias=True
            dumped_with_alias = guardian_instance.model_dump(by_alias=True)  # Замени None
            pprint.pprint(dumped_with_alias if dumped_with_alias else "Словарь (с алиасами) не был создан.")
            print("\nВыгрузка данных с Python-именами (по умолчанию):")
            # ТВОЙ КОД ЗДЕСЬ: Получи словарь из guardian_instance без опции by_alias
            dumped_without_alias = guardian_instance.model_dump()  # Замени None
            pprint.pprint(dumped_without_alias if dumped_without_alias else "Словарь (без алиасов) не был создан.")
        else:
            print("Экземпляр guardian_instance не был создан.") 
    except ValidationError as e:
        print(f"Ошибка при создании/валидации объекта:\n{e}")
    except Exception as e:
        print(f"Произошла другая ошибка: {e}")
else:
    print("Класс LegacyGuardianData еще не определен.")
print("-" * 40)



# Ожидаемый результат (после того, как ты напишешь код):
# --- Задание 7: Интеграция с Устаревшей Системой ---
# Объект успешно создан из данных с camelCase ключами.
# ID Стража (Python): PROTO-G-001
# Текущая задача (Python): Observe Entrance C
# Статус (Python): True
# Выгрузка данных с использованием алиасов (by_alias=True):
# {'guardianId': 'PROTO-G-001',
# 'currentTask': 'Observe Entrance C',
# 'isActiveStatus': True}
# Выгрузка данных с Python-именами (по умолчанию):
# {'guardian_id': 'PROTO-G-001',
# 'current_task': 'Observe Entrance C',
# 'is_active_status': True}