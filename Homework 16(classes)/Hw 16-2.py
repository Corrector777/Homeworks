import decimal
# Создайте класс DinoHealthMonitor для мониторинга здоровья динозавров в режиме
# реального времени. Класс должен:
# 1. Отслеживать основные жизненные показатели (температура, пульс, уровень
# кислорода, активность мозга, стабильность ДНК)
# 2. Иметь методы для обновления этих показателей
# 3. Содержать метод определения общего состояния здоровья на основе показателей
# 4. Генерировать предупреждения при критических изменениях
# 5. Хранить историю показателей для анализа тенденций


class DinoHealthMonitor:
    # Нормальные диапазоны показателей для динозавров (атрибуты класса)
    NORMAL_RANGES = {
        "temperature": (36.0, 38.0),  # в градусах Цельсия
        "heart_rate": (40, 80),  # ударов в минуту
        "oxygen_level": (95, 100),  # процент насыщения
        "brain_activity": (0.8, 1.0),  # относительный уровень (1.0 = оптимальный)
        "dna_stability": (0.9, 1.0)  # относительная стабильность (1.0 = идеальная)
        }

    # Ваш код: создайте конструктор класса
    # Он должен принимать: dino_id, species, age
    # Инициализировать словарь текущих показателей health_metrics
    # Создать пустой список history для истории показателей
    def __init__(self, dino_id, species, age):
        self.dino_id = dino_id
        self.species = species
        self.age = age
        self.health_metrics = {}
        self.history = []
        self.status = None

    # Ваш код: создайте метод update_metrics(temperature, heart_rate, oxygen_level, brain_activity, dna_stability)
    # Должен обновлять текущие показатели и добавлять их в историю
    # Должен вызывать метод check_health_status()
    def update_metrics(self, temperature, heart_rate, oxygen_level, brain_activity, dna_stability):
        self.health_metrics = {
            "temperature": temperature,
            "heart_rate": heart_rate,
            "oxygen_level": oxygen_level,
            "brain_activity": brain_activity,
            "dna_stability": dna_stability
        }
        self.history.append(self.health_metrics)
        self.status = self.check_health_status()
        
# Ваш код: создайте метод check_health_status()
# Должен определять общее состояние здоровья:
# "Critical" - если хотя бы один показатель сильно отклоняется от нормы
# "Warning" - если хотя бы один показатель немного отклоняется
# "Stable" - если все показатели в норме
    def check_health_status(self):
        critical_count = 0
        warning_count = 0
        for metric, value in self.health_metrics.items():
            if self.check_parameter(value, DinoHealthMonitor.NORMAL_RANGES[metric]) == "critical":
                critical_count += 1
            elif self.check_parameter(value, DinoHealthMonitor.NORMAL_RANGES[metric]) == "warning":
                warning_count += 1
        if critical_count > 0:
            return 'Critical'
        elif warning_count > 0:
            return 'Warning'
        else:
            return 'Stable'
        
    # Ваш код: создайте метод get_alerts()
    # Который возвращает список предупреждений для всех показателей,выходящих за пределы нормы
    def get_alerts(self):
        alerts = []
        for metric, value in self.health_metrics.items():
            if self.check_parameter(value, DinoHealthMonitor.NORMAL_RANGES[metric]) == "critical":
                start_tip = 'КРИТИЧНО'
                if metric == "temperature":
                    alerts.append(f"{start_tip}: Опасно высокая температура: {value}°C")
                elif metric == "heart_rate":
                    alerts.append(f"{start_tip}: Опасно высокий пульс: {value}уд/мин")
                elif metric == "oxygen_level":
                    alerts.append(f"{start_tip}: Опасно низкий уровень кислорода: {value}%")
                elif metric == "brain_activity":
                    alerts.append(f"{start_tip}: Критически низкая активность мозга: {value}")
                elif metric == "dna_stability":
                    alerts.append(f"{start_tip}: Критически низкая стабильность ДНК: {value}")
                
            elif self.check_parameter(value, DinoHealthMonitor.NORMAL_RANGES[metric]) == "warning":
                if metric == "temperature":
                    alerts.append(f"Температура выше нормы: {value}°C")
                elif metric == "heart_rate":
                    alerts.append(f"Пульс выше нормы: {value}уд/мин")
                elif metric == "oxygen_level":
                    alerts.append(f"Уровень кислорода ниже нормы: {value}%")
                elif metric == "brain_activity":
                    alerts.append(f"Активность мозга ниже нормы: {value}")
                elif metric == "dna_stability":
                    alerts.append(f"Стабильность ДНК ниже нормы: {value}")
        return alerts

    # Ваш код: создайте метод analyze_trends()
    # Который анализирует историю показателей и выявляет тенденции (улучшение/ухудшение)
    def analyze_trends(self):
        trends = {}
        if len(self.history) > 1:
            for metric, value in self.history[0].items():            
                last_value = self.history[len(self.history) - 1][metric]
                if (last_value - value) > 3:                    
                    trends[metric] = f"ухудшение (↑) +{format((last_value - value),'.1f')}"
                elif (last_value - value) < - 3:
                    trends[metric] = f"ухудшение(↓) -{format((value - last_value),'.1f')}"
                else:
                    trends[metric] = "Изменения в норме"
        else:
            raise AttributeError('Изменений нет')
        return trends


    # Ваш код: создайте метод __str__
    # Для красивого отображения текущего состояния динозавра
    def __str__(self):
        outlines = [f"ID: {self.dino_id} ({self.species}, {self.age})"]
        outlines.append(f'Статус здоровья: {self.status}')
        for metric, value in self.health_metrics.items():
            if metric == "temperature":
                outlines.append(f"Температура: {value}°C")
            elif metric == "heart_rate":
                outlines.append(f"Пульс: {value}уд/мин")
            elif metric == "oxygen_level":
                outlines.append(f"Уровень кислорода: {value}%")
            elif metric == "brain_activity":
                outlines.append(f"Активность мозга: {value}")
            elif metric == "dna_stability":
                outlines.append(f"Стабильность ДНК: {value}")
        return "\n".join(outlines)


    @staticmethod
    def check_parameter(value, normal_range):
        """Проверяет, находится ли значение в пределах нормы"""
        min_val, max_val = normal_range
        if min_val <= value <= max_val:
            return "normal"
        elif value < min_val * 0.8 or value > max_val * 1.1:
            return "critical"
        else:
            return "warning"


# Пример использования класса:
if __name__ == "__main__":
    # Создаем объект мониторинга для конкретного динозавра
    raptor_monitor = DinoHealthMonitor("VR-104", "Velociraptor", 2)

    # Обновляем показатели здоровья (нормальные значения)
    raptor_monitor.update_metrics(37.2, 65, 98, 0.95, 0.98)
    print(raptor_monitor)
    print(f"Alerts: {raptor_monitor.get_alerts()}\n")

    # Обновляем со значениями, вызывающими предупреждение
    raptor_monitor.update_metrics(38.5, 90, 94, 0.75, 0.92)
    print(raptor_monitor)
    print(f"Alerts: {raptor_monitor.get_alerts()}\n")

    # # Обновляем с критическими значениями
    # raptor_monitor.update_metrics(42.0, 120, 70, 0.6, 0.7)
    # print(raptor_monitor)
    # print(f"Alerts: {raptor_monitor.get_alerts()}\n")


# Анализируем тенденции
print("\nТенденции показателей здоровья:")
try:
    trends = raptor_monitor.analyze_trends()
    for metric, trend in trends.items():
        print(f"{metric}: {trend}")
except Exception as e:
    print(e)