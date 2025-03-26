class DinoRegistry:
# Атрибуты класса
    registered_species = [] # Список всех зарегистрированных видов
    eras = {
    "Triassic": "252-201 млн лет назад",
    "Jurassic": "201-145 млн лет назад",
    "Cretaceous": "145-66 млн лет назад"
    }
    diets = ["Carnivore", "Herbivore", "Omnivore"]
    # Статистика по эпохам
    species_by_era = {"Triassic": 0, "Jurassic": 0, "Cretaceous": 0}
    # Ваш код: создайте конструктор класса
    # Он должен принимать: name, species, era, length, weight, diet
    # И обновлять статистику по эпохам

    def __init__(self, name, species, era, length, weight, diet):
        self.name = name
        self.species = species
        self.era = era
        self.length = length
        self.weight = weight
        self.diet = diet
        DinoRegistry.species_by_era[era] += 1    
   
    # Ваш код: создайте метод classify_by_size()
    # который возвращает размерную категорию динозавра
    # "Small" (<3м), "Medium" (3-10м), "Large" (10-20м), "Colossal" (>20м)
    def classify_by_size(self):
        if self.length < 3:
            return "Small"
        elif 3 <= self.length <= 10:
            return "Medium"
        elif 10 < self.length <= 20:
            return "Large"
        elif self.length > 20:
            return "Colossal"
   
    # Ваш код: создайте метод add_to_registry()
    # Который добавляет вид в registered_species, если его там еще нет
    def add_to_registry(self):
        if self.species not in DinoRegistry.registered_species:
            DinoRegistry.registered_species.append(self.species)
            return f'Вид {self.species} добавлен в реестр'
    
    # Ваш код: создайте метод get_species_stats()
    # Который возвращает статистику по всем видам
    def get_species_stats():
        all_registered = len(DinoRegistry.registered_species)
        by_era_statistics = DinoRegistry.species_by_era
        return f"Всего зарегистрировано: {all_registered} видов.\nПо эрам:\n\
- Triassic = {by_era_statistics["Triassic"]}\n- Jurassic = {by_era_statistics["Jurassic"]}\n- Cretaceous = {by_era_statistics["Cretaceous"]}"
    
    # Ваш код: создайте метод __str__
    # Для красивого отображения информации о динозавре
    def __str__(self):
        return f"{self.name} ({self.species})\nЭра: {self.era}\nРазмеры: {self.length} м, {self.weight} кг\n\
Тип питания: {self.diet}\n"

    @classmethod
    def validate_era(cls, era):
        """Проверяет, корректна ли указанная эра"""
        return era in cls.eras

    @classmethod
    def print_all_eras(cls):
        """Выводит все известные эры и их временные промежутки"""
        for era, time_range in cls.eras.items():
            print(f"{era}: {time_range}")

# Пример использования:
if __name__ == "__main__":
# Регистрация нескольких динозавров
    trex = DinoRegistry("Tyrannosaurus Rex", "Tyrannosaurus", "Cretaceous",
    12, 8000, "Carnivore")
    stego = DinoRegistry("Spike", "Stegosaurus", "Jurassic", 9, 5000,
    "Herbivore")
    raptor = DinoRegistry("Swift", "Velociraptor", "Cretaceous", 2, 15,
    "Carnivore")
    bronto = DinoRegistry("Thunder", "Brontosaurus", "Jurassic", 22, 30000,
    "Herbivore")

# Вывод информации
    print(trex)
    print(f"Размерная категория: {trex.classify_by_size()}\n")

    # Добавление видов в реестр
    for dino in [trex, stego, raptor, bronto]:
        print(dino.add_to_registry())

    # Вывод статистики
    print("\nСтатистика видов:")
    print(DinoRegistry.get_species_stats())

    # Проверка валидности эры
    test_era = "Paleogene"
    print(f"\nЯвляется ли {test_era} корректной эрой? {DinoRegistry.validate_era(test_era)}")
    print("\nИзвестные эры динозавров:")
    DinoRegistry.print_all_eras()