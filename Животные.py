from abc import ABC, abstractmethod

# Абстрактная стратегия поведения
class BehaviorStrategy(ABC):
    @abstractmethod
    def perform(self, name):
        pass

# Конкретные стратегии поведения
class MeowStrategy(BehaviorStrategy):
    def perform(self, name):
        print(f"{name} мяукает: Мяу-мяу!")

class FlyStrategy(BehaviorStrategy):
    def perform(self, name):
        print(f"{name} взлетает в небо!")

class SwimStrategy(BehaviorStrategy):
    def perform(self, name):
        print(f"{name} плывёт в воде!")

# Базовый класс животного
class Animal:
    def __init__(self, name, behavior: BehaviorStrategy):
        self.name = name
        self.behavior = behavior

    def act(self):
        self.behavior.perform(self.name)

# Конкретные животные
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, MeowStrategy())

class Eagle(Animal):
    def __init__(self, name):
        super().__init__(name, FlyStrategy())

class Duck(Animal):
    def __init__(self, name):
        super().__init__(name, SwimStrategy())

# Пример использования
cat = Cat("Барсик")
eagle = Eagle("Петя")
duck = Duck("Гена")

cat.act()     
eagle.act()   
duck.act()    
