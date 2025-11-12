from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def attack(self):
        pass
    
    @abstractmethod
    def defend(self):
        pass
    
class Warrior(Character):
    def __init__(self,sterenghth_lvl):
        self.steringth = sterenghth_lvl
    
    def attack(self):
        return f"Воин атакует с силой {self.steringth}!"
    
    def defend(self):
        return f"Воин поднял щит! Защита +{self.steringth}"

class Mage(Character):
    def __init__(self,mana_lvl):
        self.mana = mana_lvl
        
    def attack(self):
        return f"Маг использовал заклинание! Потрачено {self.mana} маны"
    
    def defend(self):
        return f"маг использовал щит! осталось {self.mana} маны"

class Archer(Character):
    def __init__(self,accuracy):
        self.accuracy = accuracy
        
    def attack(self):
        return f"Лучник стреляет! Точность {self.accuracy}%"
    
    def defend(self):
        return f"Лучник уклонился! Шанс уклонения {self.accuracy}%"
    
def main():
    warrior = Warrior(10)
    mage = Mage(50)
    archer = Archer(80)
    
    print(warrior.attack())
    print(warrior.defend())
    
    print(mage.attack())
    print(mage.defend())
    
    print(archer.attack())
    print(archer.defend())

if __name__ == "__main__":
    main()
