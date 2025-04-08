from pydantic import BaseModel, ValidationError
import json     # Не нужен для Pydantic, но может быть полезен для создания JSON
# --- Модель данных ---
# ТВОЙ КОД ЗДЕСЬ: Определи класс TombSensorReading
# - sensor_id: str
# - timestamp: str
# - temperature: float
# - humidity: float


class TombSensorReading(BaseModel):
    sensor_id: str
    timestamp: str
    temperature: float
    humidity: float


# --- Входные данные ---
sensor_json_data = """
    {
    "sensor_id": "TOMB-TEMP-01A",
    "timestamp": "2077-10-27T10:35:11Z",
    "temperature": 15.5,
    "humidity": 88.1
    }
    """

sensor_dict_data = {
    "sensor_id": "TOMB-HUMID-02B",
    "timestamp": "2077-10-27T10:36:05Z",
    "temperature": 15.6,
    "humidity": 90.3
}

# Невалидные данные (температура - строка)
invalid_sensor_json = """
    {
    "sensor_id": "TOMB-ERR-001",
    "timestamp": "2077-10-27T10:37:00Z",
    "temperature": "очень холодно",
    "humidity": 50.0
    }
    """



# --- Логика скрипта ---
print("--- Задание 6: Прием Данных с Датчиков ---")
# TombSensorReading = None # Заглушка
# ВАЖНО: Когда ты определишь класс TombSensorReading выше, удали или закомментируй эту строку
if TombSensorReading:
    print("\n1. Десериализация из JSON:")
    try:
        # ТВОЙ КОД ЗДЕСЬ: Создай экземпляр reading_from_json из sensor_json_data
        # Используй метод класса model_validate_json()
        reading_from_json = TombSensorReading.model_validate_json(sensor_json_data)  # Замени None
        if reading_from_json:
            print("Успешно создано из JSON:")
            print(reading_from_json.model_dump())
        else:
            print("Экземпляр reading_from_json не создан.")
    except ValidationError as e:
        print(f"Ошибка при десериализации JSON:\n{e}")
    except Exception as e:
        print(f"Другая ошибка при десериализации JSON: {e}")

    print("\n2. Десериализация из Словаря:")
    try:
        # ТВОЙ КОД ЗДЕСЬ: Создай экземпляр reading_from_dict из sensor_dict_data
        # Используй распаковку словаря **
        reading_from_dict = TombSensorReading(**sensor_dict_data)  # Замени None
        if reading_from_dict:
            print("Успешно создано из Словаря:")
            print(reading_from_dict.model_dump())
        else:
            print("Экземпляр reading_from_dict не создан.")
    except ValidationError as e:
        print(f"Ошибка при десериализации Словаря:\n{e}")
    except Exception as e:
        print(f"Другая ошибка при десериализации из Словаря: {e}")

    print("\n3. Десериализация невалидного JSON:")
    try:
        # ТВОЙ КОД ЗДЕСЬ: Попытайся создать экземпляр из invalid_sensor_json
        invalid_reading = TombSensorReading.model_validate_json(invalid_sensor_json)  # Замени None
        if invalid_reading:
            print("Успешно создано из невалидного JSON (Этого не должно быть)")
        else:
            # Ожидаемое поведение, если парсинг/валидация не удались
            pass
    except ValidationError as e:
        print("Ожидаемая ошибка при десериализации невалидного JSON:")
        print(e) # Выведет информацию об ошибке валидации типа
    except Exception as e:
        print(f"Другая ошибка при десериализации невалидного JSON: {e}")
else:
    print("Класс TombSensorReading еще не определен.")
    print("-" * 40)


# Ожидаемый результат (после того, как ты напишешь код):
# --- Задание 6: Прием Данных с Датчиков ---
# 1. Десериализация из JSON:
# Успешно создано из JSON:
# {'sensor_id': 'TOMB-TEMP-01A', 'timestamp': '2077-10-27T10:35:11Z',
# 'temperature': 15.5, 'humidity': 88.1}
# 2. Десериализация из Словаря:
# Успешно создано из Словаря:
# {'sensor_id': 'TOMB-HUMID-02B', 'timestamp': '2077-10-27T10:36:05Z',
# 'temperature': 15.6, 'humidity': 90.3}
# 3. Десериализация невалидного JSON:
# Ожидаемая ошибка при десериализации невалидного JSON:
# 1 validation error for TombSensorReading
# temperature
# Input should be a valid number, unable to parse string as a number
# [type=float_parsing, input_value='очень холодно', input_type=str]
# For further information visit
# https://errors.pydantic.dev/2.7/v/float_parsing