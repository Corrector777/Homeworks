import datetime
# Задание
# Создайте класс GeneticConstructor с многоуровневой защитой данных. Класс должен:
# 1. Использовать защищенные атрибуты (с одним подчеркиванием _ ) для базовых
# данных
# 2. Использовать "приватные" атрибуты (с двумя подчеркиваниями __ ) для критических
# данных
# 3. Включать геттеры и сеттеры для безопасного доступа к данным
# 4. Реализовать систему авторизации с уровнями доступа
# 5. Фиксировать все попытки доступа к защищенным данным
# 6. Генерировать предупреждения при попытках несанкционированного доступа


class GeneticConstructor:
    """Класс для безопасного конструирования и хранения генетических
    последовательностей динозавров"""
    # Уровни доступа
    ACCESS_LEVELS = {
        "public": 0,  # Публичная информация
        "restricted": 1,  # Ограниченный доступ
        "confidential": 2, # Конфиденциальная информация
        "secret": 3  # Секретная информация
        }
# Авторизованные коды доступа
    AUTHORIZED_CODES = {
        "PUBLIC": ("public", 0),  # Может просматривать только публичные данные
        "LAB-ASSISTANT": ("restricted", 1),  # Может просматривать ограниченные данные
        "SCIENTIST": ("confidential", 2),  # Может просматривать конфиденциальные данные
        "DIRECTOR": ("secret", 3) # Полный доступ ко всем данным
        }
    
    def __init__(self, project_name, species, lead_scientist):
        # Публичные атрибуты
        self.project_name = project_name
        # Защищенные атрибуты (с одним подчеркиванием)
        self._species = species
        self._lead_scientist = lead_scientist
        self._creation_date = datetime.datetime.now()
        self._modification_history = []
        # Журнал доступа
        self._access_log = []
        self._unauthorized_attempts = 0
        # "Приватные" атрибуты (с двумя подчеркиваниями)
        self.__dna_sequence = ""
        self.__stability_factor = 0.0
        self.__mutation_probability = 0.0
        self.__gene_modifications = []

    # Ваш код: создайте геттеры и сеттеры для защищенных атрибутов
    # get_species(), set_species(), get_lead_scientist(), set_lead_scientist()
    def get_species(self, access_code, required_level='restricted'):
        method_name = 'get_species'
        if self.validate_access_code(access_code, required_level, method_name):
            return self._species
        else:
            return f'[Доступ запрещен] Необходим уровень доступа не ниже: {required_level}'
        
    def set_species(self, access_code, value, required_level='restricted'):
        method_name = self.set_species.__name__
        if self.validate_access_code(access_code, required_level, method_name):         
            self._species = value
            self._modification_history.append(f'{self._creation_date.strftime("%Y-%m-%d %H:%M:%S")} {method_name}: Изменен вид на: {self._species} ({access_code})\n')  
        else:
            return f'[Доступ запрещен] Необходим уровень доступа не ниже: {required_level}'

    def get_lead_scientist(self, access_code, required_level='restricted'):
        method_name = self.set_lead_scientist.__name__
        if self.validate_access_code(access_code, required_level, method_name):
            return self._lead_scientist
        else:
            return f'[Доступ запрещен] Необходим уровень доступа не ниже: {required_level}'

    def set_lead_scientist(self, access_code, value, required_level='restricted'):
        method_name = self.set_lead_scientist.__name__
        if self.validate_access_code(access_code, required_level, method_name):
            self._lead_scientist = value
            self._modification_history.append(f'{self._creation_date.strftime("%Y-%m-%d %H:%M:%S")} {method_name}: Изменен руководитель на: {self._lead_scientist} ({access_code})\n')
        else:
            return f'[Доступ запрещен] Необходим уровень доступа не ниже: {required_level}'

    # Ваш код: создайте методы для работы с "приватными" атрибутами
    # Методы должны проверять уровень доступа:    
    # get_dna_sequence(access_code), set_dna_sequence(access_code, new_sequence)
    def get_dna_sequence(self, access_code, required_level='confidential'):
        method_name = self.get_dna_sequence.__name__
        if self.validate_access_code(access_code, required_level, method_name):
            return self.__dna_sequence
        else:
            return f'[Доступ запрещен] Необходим уровень доступа не ниже: {required_level}'

    def set_dna_sequence(self, access_code, new_sequence, required_level='confidential'):
        method_name = self.set_dna_sequence.__name__
        if self.validate_access_code(access_code, required_level, method_name):
            self.__dna_sequence = new_sequence
            self._modification_history.append(f'{self._creation_date.strftime("%Y-%m-%d %H:%M:%S")} {method_name}: Изменен DNA на: {self.__dna_sequence} ({access_code})\n')
        else:
            return f'[Доступ запрещен] Необходим уровень доступа не ниже: {required_level}'
    
    # get_stability_factor(access_code), set_stability_factor(access_code, value)
    def get_stability_factor(self, access_code, required_level='confidential'):
        method_name = self.get_stability_factor.__name__
        if self.validate_access_code(access_code, required_level, method_name):
            return self.__stability_factor
        else:
            return f'[Доступ запрещен] Необходим уровень доступа не ниже: {required_level}'

    def set_stability_factor(self, access_code, value, required_level='confidential'):
        method_name = self.set_stability_factor.__name__
        if self.validate_access_code(access_code, required_level, method_name):
            self.__stability_factor = value
            self._modification_history.append(f'{self._creation_date.strftime("%Y-%m-%d %H:%M:%S")} {method_name}: Изменен коэффициент стабильности на: {self.__stability_factor} ({access_code})\n')     
        else:
            return f'[Доступ запрещен] Необходим уровень доступа не ниже: {required_level}'

    # get_mutation_probability(access_code), set_mutation_probability(access_code, value)
    def get_mutation_probability(self, access_code, required_level='confidential'):
        method_name = self.get_mutation_probability.__name__        
        if self.validate_access_code(access_code, required_level, method_name):
            return self.__mutation_probability
        else:
            return f'[Доступ запрещен] Необходим уровень доступа не ниже: {required_level}'

    def set_mutation_probability(self, access_code, value, required_level='confidential'):
        method_name = self.set_mutation_probability.__name__
        if self.validate_access_code(access_code, required_level, method_name):
            self.__mutation_probability = value
            self._modification_history.append(f'{self._creation_date.strftime("%Y-%m-%d %H:%M:%S")} {method_name}: Изменена вероятность мутации на: {self.__mutation_probability} ({access_code})\n')            
            

    # Ваш код: создайте метод add_gene_modification(access_code, modification)
    # Который добавляет новую модификацию гена при наличии нужного уровня доступа
    def add_gene_modification(self, access_code, modification, required_level='confidential'):
        method_name = self.add_gene_modification.__name__
        if self.validate_access_code(access_code, required_level, method_name):
            self.__gene_modifications.append(modification)
            self._modification_history.append(f'{self._creation_date.strftime("%Y-%m-%d %H:%M:%S")} {method_name}: Добавлена модификация гена: {modification} ({access_code})\n')
        else:
            return f'[Доступ запрещен] Необходим уровень доступа не ниже: {required_level}'

    # Ваш код: создайте метод validate_access_code(access_code, required_level)
    # Для проверки прав доступа и логирования попыток несанкционированного доступа    
    def validate_access_code(self, access_code, required_level, method_name):       
        if access_code in GeneticConstructor.AUTHORIZED_CODES and GeneticConstructor.AUTHORIZED_CODES[access_code][1] >= GeneticConstructor.ACCESS_LEVELS[required_level]:
            self._access_log.append(f'{self._creation_date.strftime("%Y-%m-%d %H:%M:%S")} {method_name}: Успешно ({access_code})')
            return True
        else:
            self._access_log.append(f'{self._creation_date.strftime("%Y-%m-%d %H:%M:%S")} {method_name}: ОТКАЗАНО ({access_code}) - Недостаточный уровень доступа')
            self._unauthorized_attempts += 1
            return False
    
    # Ваш код: создайте метод get_access_log()
    # Который возвращает журнал доступа (только для уровня DIRECTOR)
    def get_access_log(self, access_code, required_level='secret'):
        method_name = self.get_access_log.__name__
        result_str = ''
        if self.validate_access_code(access_code, required_level, method_name):
            for log in self._access_log:
                result_str += log + '\n'
            return result_str
        else:
            return f'[Доступ запрещен] Необходим уровень доступа не ниже: {required_level}'

    # Ваш код: создайте метод __str__
    # Для отображения публичной информации о проекте
    def __str__(self):
        return f"Проект: {self.project_name}\nВид: [Доступ ограничен]\nРуководитель: [Доступ ограничен]\nДата создания: {self._creation_date.strftime('%Y-%m-%d %H:%M:%S')}"

# Пример использования:
if __name__ == "__main__":
    # Создаем генетический проект
    trex_project = GeneticConstructor("Rex-Alpha", "Tyrannosaurus Rex", "Dr.Ellie Hammond")
    # Получаем публичную информацию
    print(trex_project)
    # Пробуем получить доступ к защищенным данным с разными кодами доступа
    print("\nПопытки доступа к защищенным данным:")
    # Ограниченный доступ
    print(f"Вид (LAB-ASSISTANT): {trex_project.get_species('LAB-ASSISTANT')}")
    trex_project.set_lead_scientist('LAB-ASSISTANT', 'Dr. Alan Grant')
    print(f"Новый руководитель: {trex_project.get_lead_scientist('LAB-ASSISTANT')}")
    # # Попытка неавторизованного доступа
    print(f"Попытка получить ДНК с кодом LAB-ASSISTANT: {trex_project.get_dna_sequence('LAB-ASSISTANT')}")
    # # Авторизованный доступ
    trex_project.set_dna_sequence('SCIENTIST', "ACGTAGCTAGCTAGCAGTCGTAGCTAGCTAGC")
    print(f"ДНК (SCIENTIST): {trex_project.get_dna_sequence('SCIENTIST')}")
    # # Устанавливаем параметры с высоким уровнем доступа
    trex_project.set_stability_factor('DIRECTOR', 0.89)
    trex_project.set_mutation_probability('DIRECTOR', 0.05)
    # # Добавляем генетические модификации
    trex_project.add_gene_modification('SCIENTIST', "Enhanced muscle growth")
    trex_project.add_gene_modification('DIRECTOR', "Temperature adaptation")
    # # Пытаемся добавить модификацию с недостаточным уровнем доступа
    trex_project.add_gene_modification('LAB-ASSISTANT', "Unauthorized modification")
    # # Просматриваем журнал доступа
    print("\nЖурнал доступа (SCIENTIST):")
    print(trex_project.get_access_log('SCIENTIST'))
    print("\nЖурнал доступа (DIRECTOR):")
    print(trex_project.get_access_log('DIRECTOR'))
   
    # # Выводим статистику несанкционированных попыток
    print(f"Несанкционированных попыток доступа: {trex_project._unauthorized_attempts}")

    print('\n\nИстория изменений:\n')
    for i in trex_project._modification_history:
        print(i)
