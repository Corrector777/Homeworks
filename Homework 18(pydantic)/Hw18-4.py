# task_4_custom_validator.py
from pydantic import BaseModel, ValidationError, field_validator  # Используем field_validator из V2
# --- Данные от энергоядер ---
core_data_ok = {"core_id": "PC-Omega-7", "energy_percent": 75}
core_data_high = {"core_id": "PC-Alpha-1", "energy_percent": 110}  # Невалидное
core_data_low = {"core_id": "PC-Beta-3", "energy_percent": -5}  # Невалидное
# --- Модели ---


# ТВОЙ КОД ЗДЕСЬ: Определи класс PowerCoreStatus
class PowerCoreStatus(BaseModel):
    core_id: str
    energy_percent: int 

    # - Добавь метод-валидатор для 'energy_percent' с декоратором
    @field_validator('energy_percent')
    @classmethod
    def check_energy_range(cls, v: int):
        # Внутри метода: проверь v (значение). Если не в [0, 100], то raise # ValueError(...)
        print(f"Проверка значения energy_percent: {v}")  # Лог для наглядности
        #  ... твоя логика проверки и return/raise ...
        if 0 <= v <= 100:
            return v
        else:
            raise ValueError(f'Value error, Уровень энергии должен быть от 0 до 100, получено: {v}') # raise ValueError


# --- Логика скрипта ---
print("--- Задание 4: Проверка Энергоядра ---")
# PowerCoreStatus = None # Заглушка
# ВАЖНО: Когда ты определишь класс PowerCoreStatus выше, удали или закомментируй эту строку
if PowerCoreStatus is not None:
    print("\nТест 1: Валидные данные")
    try:
        # ТВОЙ КОД ЗДЕСЬ: Создай экземпляр PowerCoreStatus из core_data_ok
        core_ok = PowerCoreStatus(**core_data_ok) # Замени None
        if core_ok:
            print(f"Успешно создан статус ядра: {core_ok.core_id} с энергией {core_ok.energy_percent}%")
            print(f"Данные: {core_ok.model_dump()}")
        else:
            print("Экземпляр core_ok не создан.")
    except ValidationError as e:
        print(f"Ошибка валидации: {e}")
    except Exception as e:
        print(f"Другая ошибка в Тесте 1: {e}")

    print("\nТест 2: Слишком высокий уровень энергии")
    try:
        # ТВОЙ КОД ЗДЕСЬ: Создай экземпляр PowerCoreStatus из core_data_high
        core_high = PowerCoreStatus(**core_data_high) # Замени None
        if core_high:
            print(f"Успешно создан статус ядра: {core_high.core_id}") # Не должно выполниться
        else:
            # Это ожидаемое поведение, если валидатор сработал
            pass
    except ValidationError as e:
        print(f"Ожидаемая ошибка валидации:")
        print(e)
    except Exception as e:
        print(f"Другая ошибка в Тесте 2: {e}")
    
    print("\nТест 3: Отрицательный уровень энергии")
    try:
        # ТВОЙ КОД ЗДЕСЬ: Создай экземпляр PowerCoreStatus из core_data_low
        core_low = PowerCoreStatus(**core_data_low) # Замени None
        if core_low:
            print(f"Успешно создан статус ядра: {core_low.core_id}") # Не должно выполниться
        else:
            # Это ожидаемое поведение, если валидатор сработал
            pass
    except ValidationError as e:
        print(f"Ожидаемая ошибка валидации:")
        print(e)
    except Exception as e:
        print(f"Другая ошибка в Тесте 3: {e}")
else:
    print("Класс PowerCoreStatus еще не определен.")
    print("-" * 40)

# Ожидаемый результат (после того, как ты напишешь код):
# --- Задание 4: Проверка Энергоядра ---
# Тест 1: Валидные данные
# Проверка значения energy_percent: 75
# Успешно создан статус ядра: PC-Omega-7 с энергией 75%
# Данные: {'core_id': 'PC-Omega-7', 'energy_percent': 75}
# Тест 2: Слишком высокий уровень энергии
# Проверка значения energy_percent: 110
# Ожидаемая ошибка валидации:
# 1 validation error for PowerCoreStatus
# energy_percent
# Value error, Уровень энергии должен быть от 0 до 100, получено: 110
# [type=value_error, input_value=110, input_type=int]
# For further information visit
# https://errors.pydantic.dev/2.7/v/value_error
# Тест 3: Отрицательный уровень энергии
# Проверка значения energy_percent: -5
# Ожидаемая ошибка валидации:
# 1 validation error for PowerCoreStatus
# energy_percent
# Value error, Уровень энергии должен быть от 0 до 100, получено: -5
# [type=value_error, input_value=-5, input_type=int]
# For further information visit
# https://errors.pydantic.dev/2.7/v/value_error