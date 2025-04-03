from pydantic import BaseModel, ValidationError


# Ваша задача: Определить Pydantic модель SphinxUnit с полями unit_id (строка),
# model_version (целое число) и is_active (булево). Затем создать экземпляр этой
# модели, используя предоставленный словарь unit_data , и вывести атрибуты созданного
# объекта.

# --- Данные от первого попавшегося юнита ---
# Представь, что эти данные пришли по сети в виде словаря
unit_data = {
"unit_id": "SPX-07-ALPHA",
"model_version": 3,
"is_active": True
}
# --- Модели ---
# ТВОЙ КОД ЗДЕСЬ: Определи класс SphinxUnit, наследующийся от BaseModel
# Он должен иметь поля:
# - unit_id: строка (str)
# - model_version: целое число (int)
# - is_active: булево (bool)

class SphinxUnit(BaseModel):
    unit_id: str
    model_version: int
    is_active: bool

# --- Логика скрипта ---
print("--- Задание 1: Базовый Профиль Юнита ---")
sphinx_instance = None # Инициализируем переменную
try:
# ТВОЙ КОД ЗДЕСЬ: Создай экземпляр SphinxUnit из словаря unit_data
# Используй распаковку словаря (**unit_data)
# Замени None на создание экземпляра
    sphinx_instance = SphinxUnit(**unit_data)


# Этот код должен сработать, если создание экземпляра прошло успешно
    if sphinx_instance:
        print("Экземпляр SphinxUnit успешно создан!")
        print(f"ID Юнита: {sphinx_instance.unit_id}")
        print(f"Версия Модели: {sphinx_instance.model_version}")
        print(f"Статус Активности: {sphinx_instance.is_active}")
        print(f"Представление объекта: {sphinx_instance}")
    else:
    # Если ты не создал экземпляр, выведем сообщение
        print("Экземпляр SphinxUnit не был создан. Начни с определения класса!")
except ValidationError as e:
    print(f"Ошибка валидации при создании объекта:\n{e}")
except NameError:
    print("Класс SphinxUnit еще не определен!")
except Exception as e:
    print(f"Произошла другая ошибка: {e}")
    print("-" * 40)


# Ожидаемый результат (после того, как ты напишешь код):

# --- Задание 1: Базовый Профиль Юнита ---
# Экземпляр SphinxUnit успешно создан!
# ID Юнита: SPX-07-ALPHA
# Версия Модели: 3
# Статус Активности: True
# Представление объекта: unit_id='SPX-07-ALPHA' model_version=3 is_active=True