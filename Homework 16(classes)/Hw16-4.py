import random
# 1. __init__ для инициализации параметров динозавра (имя, вид, сила, скорость,
# интеллект)
# 2. __str__ и __repr__ для читаемого представления объекта
# 3. Операторы сравнения ( __lt__ , __gt__ , __eq__ ) для сопоставления динозавров по
# силе
# 4. __add__ для "скрещивания" двух динозавров (создания нового с комбинированными
# характеристиками)
# 5. __call__ для выполнения действий (охота, решение задач, бег)
# 6. __len__ для получения "размера" динозавра (общей оценки характеристик)


class DinoSimulation:
    """Класс для симуляции поведения динозавров с использованием специальных
    методов"""
    def __init__(self, name, species, strength, speed, intelligence):
        # Ваш код: инициализируйте атрибуты
        # self.name, self.species, self.strength, self.speed, self.intelligence
        self.name = name
        self.species = species
        self.strength = strength
        self.speed = speed
        self.intelligence = intelligence

        # Рассчитайте общую оценку на основе атрибутов
        self.total_score = self.strength + self.speed + self.intelligence
    
    # Ваш код: создайте методы __str__ и __repr__
    # для удобного представления объекта при печати
    def __str__(self):
        return f"{self.name} ({self.species}) Strength: {self.strength}, Speed: {self.speed}, Intelligence: {self.intelligence}, Total: {self.total_score}\n"

    # Ваш код: создайте методы сравнения __lt__, __gt__, __eq__
    # для сравнения динозавров по атрибуту strength
    def __lt__(self, other):
        return self.strength < other.strength
    
    def __gt__(self, other):
        return self.strength > other.strength
    
    def __eq__(self, other):
        return self.strength == other.strength
    
    # Ваш код: создайте метод __add__
    # который создает нового динозавра-гибрида с усредненными характеристиками
    # кроме name (должно быть '{name1}+{name2}')
    # и species (должно быть '{species1}-{species2} Hybrid')
    def __add__(self, other):
        name = f"{self.name}+{other.name}"
        species = f"{self.species}-{other.species} Hybrid"
        strength = round((self.strength + other.strength) / 2, 1)
        speed = round((self.speed + other.speed) / 2, 1)
        intelligence = round((self.intelligence + other.intelligence) / 2, 1)
        return DinoSimulation(name, species, strength, speed, intelligence)

    # Ваш код: создайте метод __call__(action_type, target=None)
    # который симулирует выполнение различных действий:
    # - "hunt": пытается охотиться на цель, успех зависит от силы и скорости
    # - "solve": решает головоломку, успех зависит от интеллекта
    # - "run": бежит, возвращает скорость
    def __call__(self, action_type, target=None):
        if action_type == "hunt":
            hunt_flag = 'Провал!'
            if target:
                hunt_success = ((self.strength + self.speed) - (target.speed + target.strength)) / 10
                if random.random() < hunt_success:
                    hunt_flag = 'Успешно!'
                return f"{self.name} охотится на {target.name}... {hunt_flag} Разница в силе: {self.strength - target.strength:.1f}" 
                
            else:
                return "Цель не указана"               
           
        elif action_type == "solve":
            solve_flag = 'Провал!'
            if random.random() < self.intelligence / 10:
                solve_flag = 'Успешно!'
            return f"{self.name} решает головоломку... {solve_flag} Интеллект: {self.intelligence}"
        
        elif action_type == "run":
            return f'{self.name} бежит со скоростью: {self.speed}'
        
    # Ваш код: создайте метод __len__
    # который возвращает общую оценку, округленную до целого числа
    def __len__(self):
        return round(self.total_score)

    # Добавьте метод simulate_day()
    # который возвращает серию действий, выполняемых динозавром в течение дня
    def simulate_day(self):
        simulate = f'Утро: Rex просыпается и осматривает территорию\n\
Полдень: Rex охотится и ловит добычу (шанс успеха: {(self.strength / 10 + self.speed / 10) / 2 * 100}%)\n\
Вечер: Rex отдыхает после успешной охоты\n\
Ночь: Rex спит, восстанавливая силы'
        return simulate


# Пример использования:
if __name__ == "__main__":
    # Создаем динозавров для симуляции
    trex = DinoSimulation("Rex", "Tyrannosaurus", 9.6, 7.0, 6.0)
    raptor = DinoSimulation("Blue", "Velociraptor", 6.0, 9.5, 8.5)
    trice = DinoSimulation("Cera", "Triceratops", 8.0, 5.5, 4.5)
    # Выводим информацию
    print(trex)
    print(raptor)
    # Сравниваем динозавров
    print(f"T-Rex сильнее Раптора? {trex > raptor}")
    print(f"Раптор сильнее Трицератопса? {raptor > trice}")
    print(f"T-Rex и Трицератопс одинаково сильны? {trex == trice}")
    # # Создаем гибридного динозавра
    hybrid = trex + raptor
    print(hybrid)
    # # Выполняем действия
    # Ожидаемый вывод
    print(trex("hunt", raptor))
    print(raptor("solve"))
    print(trice("run"))
    # # Получаем "размер" (общую оценку) динозавра
    print(f"Общая оценка T-Rex: {len(trex)}")
    print(f"Общая оценка Раптора: {len(raptor)}")
    print(f"Общая оценка гибрида: {len(hybrid)}")
    # # Симулируем день
    print("\nДень из жизни T-Rex:")
    print(trex.simulate_day())