class computer:
    def __init__(self):
         self.cpu = None
         self.ram = None
         self.storage = None
         self.gpu = None
         self.components = [] # - Список для хранения дополнительных комплектующих
         
    def __str__(self):
        # Метод для строкового представления объекта компьютера
        # Формирует читаемую строку со всеми характеристиками
        return (f"Компьютер: \nЦП={self.cpu}\nОЗУ={self.ram}\n"
                f"накопитель={self.storage}\nВидеокарта={self.gpu}\n"
                f"Комплектующие={self.components}")
        
class ComputerBuilder:
       # Создаём новый объекты компьютера при инициализации строителя
    def __init__(self):
        self.computer = computer()
        
    def set_cpu(self,cpu):
        self.computer.cpu = cpu
        return self
    
    def set_ram(self,ram):
        self.computer.ram = ram
        return self
        
    def set_storage(self, storage):
        self.computer.storage = storage
        return self
    
    def set_gpu(self,gpu):
        self.computer.gpu = gpu
        return self
    
    def add_component(self,component):
        self.computer.components.append(component)
        return self
    
    def build(self):
        return self.computer

builder = ComputerBuilder()
computer = (builder.set_cpu("Intel i7")
               .set_ram("32 ГБ")
               .set_storage("1 ТБ SSD")
               .set_gpu("NVIDIA RTX 4080")
               .add_component("Wi-Fi адаптер")
               .add_component("Звуковая карта")
               .build())

print(computer)