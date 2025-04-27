import json
import requests
from datetime import datetime
import os

# === Загрузка/сохранение настроек ===
def load_config() -> dict:
    """Загружает конфигурацию из файла config.json"""
    try:
        with open('config.json') as f:
            return json.load(f)
    except FileNotFoundError:
        return {'default_city': 'Москва'}
    

def save_config(cfg: dict):
    """Сохраняет конфигурацию в файл config.json"""
    
    with open('config.json', 'w') as f:
        json.dump(cfg, f, ensure_ascii=False)


# === Геокодер ===
def geocode(city: str):
    """Возвращает координаты города по его названию"""

    url = 'https://nominatim.openstreetmap.org/search'
    params = {'city': city, 'format': 'json'}
    # во избежанию блокировки передаем данные агента
    headers = {'User-Agent': "#ROOTCONFIG#/n.n.n (powered by Rainmeter)"}
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        # print(f"Request to -{url}- successful! Status: {response.status_code}")
        # Выводим найденную локацию в формате JSON, а также координаты
        # print(f"Response geocode JSON: {response.json()}")
        lat = response.json()[0]["lat"]
        lon = response.json()[0]['lon']
        # print('lat, lon:', lat, lon)   
        return lat, lon
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
        if err.response is not None:
            print(f"Status code: {err.response.status_code}")
            print(f"Response text: {err.response.text}")
            return None


# === Вызовы API ===
def get_current(lat: str, lon: str):
    """Возвращает текущие данные о погоде"""

    url = 'https://api.open-meteo.com/v1/forecast'
    params = {
            "latitude": lat,
            "longitude": lon,
            "current": ["temperature_2m", "wind_speed_10m", "relative_humidity_2m"],
            "forecast_days": 1
            }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        # print(f"Request to -{url}- successful! Status: {response.status_code}")
        # print(f"Response JSON: {response.json()}")
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
        if err.response is not None:
            print(f"Status code: {err.response.status_code}")
            print(f"Response text: {err.response.text}")
            return None


def get_forecast(lat: str, lon: str, days: int):
    """Возвращает прогноз погоды на указанное количество дней"""
    url = 'https://api.open-meteo.com/v1/forecast'
    params = {
            "latitude": lat,
            "longitude": lon,
            "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
            "forecast_days": days,
            "forecast_hours": 24
            }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        # print(f"Request to -{url} - successful! Status: {response.status_code}")
        # print(f"Response forecast JSON: {response.json()}")
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
        if err.response is not None:
            print(f"Status code: {err.response.status_code}")
            print(f"Response text: {err.response.text}")
            return None
        

def get_history(lat: str, lon: str, date_str: str):
    """Возвращает исторические данные о погоде на указанную дату"""

    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
            "latitude": lat,
            "longitude": lon,
            "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
            "start_date": date_str,
            "end_date": date_str
             }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        # print(f"Request to -{url}- successful! Status: {response.status_code}")
        # print(f"Response JSON: {response.json()}")
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
        if err.response is not None:
            print(f"Status code: {err.response.status_code}")
            print(f"Response text: {err.response.text}")
            return None


def display_current(data: dict):
    """Выводит текущие данные о погоде"""

    temperature = data['current']['temperature_2m']
    wind_speed = data['current']['wind_speed_10m']
    relative_humidity = data['current']['relative_humidity_2m'] 
    print(f'Темп: {temperature}°C, Влажность: {relative_humidity}%, Ветер: {wind_speed} м/с')


def display_forecast(data: dict):
    """Выводит прогноз погоды на несколько дней"""

    all_dates = data['daily']['time']
    all_temp_max = data['daily']['temperature_2m_max']
    all_temp_min = data['daily']['temperature_2m_min']
    all_precip = data['daily']['precipitation_sum']
    print('  [ДАТА]     | Макс.темп(°C) | Мин.темп(°C) | Суммарные осадки(мм)')
    for i in range(len(all_dates)):
        print(f' {all_dates[i]}  |    {all_temp_max[i]}°C      |   {all_temp_min[i]}°C     |  {all_precip[i]} мм   ')


def display_history(data: dict):
    """Выводит исторические данные о погоде на указанную дату"""

    date = data['daily']['time'][0]
    temp_max = data['daily']['temperature_2m_max'][0]
    temp_min = data['daily']['temperature_2m_min'][0]
    precip = data['daily']['precipitation_sum'][0]
    print('  [ДАТА]   | Макс.темп(°C) | Мин.темп(°C) | Суммарные осадки(мм)')
    print(f'{date} |    {temp_max}°C      |   {temp_min}°C     |  {precip} мм   ')

        
def print_menu(cfg: dict):
    """Выводит главное меню и текущие данные о погоде, а также оповещения(если установлены)"""

    print(f"Привет! Город по умолчанию - {cfg["default_city"]}")
    print(f"Текущая погода для города {cfg["default_city"]}:")
    lat, lon = geocode(cfg["default_city"])
    data = get_current(lat, lon)
    display_current(data)
    # Проверка оповещения и вывод уведомлений
    if 'alert' in cfg and isinstance(cfg['alert'], list):
        print(f'Условия оповещения: мин.темп: {cfg['alert'][0]}, макс.темп: {cfg['alert'][1]}')
        current_temperature = float(data['current']['temperature_2m'])
        if current_temperature > float(cfg['alert'][1]):
            print(f"\n--Внимание!Температура выше {cfg['alert'][1]} градусов!--\n")
        elif current_temperature < float(cfg['alert'][0]):
            print(f"\n--Внимание!Температура ниже {cfg['alert'][0]} градусов!--\n")

    print("Выберите действие:")
    print("1. Текущая погода")
    print("2. Прогноз на N дней")
    print("3. История по дате")
    print("4. Установить условие оповещения")
    print("5. Сменить город по умолчанию")
    print("0. Выход")

# отладочные запросы
# lat, lon = geocode('Moscow')
# get_current(lat= lat, lon=lon)
# get_forecast(lat=lat, lon=lon, days=7)
# get_history(lat=lat, lon=lon, date_str='2022-04-14')


# # === Оповещения ===
def set_alert(cfg: dict, condition: list):
    """Устанавливает условия оповещения и сохраняет в конфигурационном файле"""

    cfg['alert'] = condition
    print('Оповещение сохранено')
    save_config(cfg)


def ask_city(cfg: dict):
    """Запрашивает у пользователя название города и возвращает его"""
    city = input("Введите город: ").strip()
    if not city:
        print(f"Выбран город по умолчанию: {cfg['default_city'].capitalize()}")
        return cfg['default_city']
    elif any(char.isdigit() for char in city):
        raise ValueError('Ошибка! В названии не может быть чисел!')   
    else:
        print(f"Выбран город: {city.capitalize()}")
        return city.capitalize()


def ask_days():
    """Запрашивает у пользователя количество дней и возвращает """

    days = input("Введите количество дней: ").strip()
    if days.isdigit():
        return days
    else:
        raise ValueError('Ошибка! Количество дней должно быть числом')


# # === Меню и ввод пользователя ===
def main_menu():
    """Основное меню программы"""
    cfg = load_config()
    while True:
        try:
            print_menu(cfg)
            choice = input("Ваш выбор (0–5): ").strip()
            if choice == '1':
                city = ask_city(cfg)
                lat, lon = geocode(city)
                data = get_current(lat, lon)
                display_current(data)
                input("Нажмите Enter…")

            elif choice == '2':
                days = ask_days()
                city = ask_city(cfg)
                lat, lon = geocode(city)
                data = get_forecast(lat, lon, days)
                print(f"Прогноз на {days} дней для города {city}:")
                display_forecast(data)
                input("Нажмите Enter…")
            
            elif choice == '3':
                date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ").strip()
                try:
                    datetime.strptime(date_str, '%Y-%m-%d')
                except ValueError:
                    raise ValueError('Ошибка! Проверьте правильность ввода даты')
                city = ask_city(cfg)
                lat, lon = geocode(city)
                data = get_history(lat, lon, date_str)
                if data is None:
                    print("\nЧто-то пошло не так. Проверьте правильность ввода даты.\n")
                    continue
                else:
                    print(f"История на дату {date_str} для города {city}:")
                    display_history(data)
                input("Нажмите Enter…")
        
            elif choice == '4':
                string = input("Введите масимальную и минимальную температуру через пробел в любом порядке: ").strip()
                cond = string.split(' ')
                if len(cond) != 2:
                    raise ValueError('Ошибка! Введите два значения температуры через пробел')   
                cond.sort(key=float)
                print(f'\nУсловия установлены: мин.темп: {cond[0]}, макс.темп: {cond[1]}\n')
                lat, lon = geocode(cfg['default_city'])
                data = get_current(lat, lon)
                set_alert(cfg, cond)
                input("Нажмите Enter…")

            elif choice == '5':
                new_city = input("Новый город по умолчанию: ").strip()
                if any(char.isdigit() for char in new_city):
                    raise ValueError('Ошибка! Город не может быть числом')
                cfg['default_city'] = new_city or cfg['default_city']
                save_config(cfg)
                input("Нажмите Enter…")
            elif choice == '0':
                print("Выход. До встречи!")
                if os.path.exists('config.json'):
                    os.remove('config.json')
                break
            else:
                print("Неверный выбор. Попробуйте ещё раз.")
        except ValueError as err:
            print('\n', err, '\n')
        except KeyError as err:
            print('\n', err, '\n')
        except Exception as err:
            print('\n', err, '\n')

if __name__ == "__main__":
    main_menu()