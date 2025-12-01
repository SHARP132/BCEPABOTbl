print("Вариант 4\nЗадание 1:")
class Media:
    def play(self):
        return "Playing media"
    
    def pause(self):
        return "Pausing media"
    
media = Media()


print(media.play())  
print(media.pause()) 

print("\nЗадание 2:")
class Employee:
    def __init__(self, name, doljnost, opit):
        self.name = name
        self.doljnost = doljnost
        self.opit = opit

    def bonus(self):
        """
        До 5 лет — 5%
        От 5 до 10 лет — 10%
        Более 10 лет — 15%
        """
        if self.opit < 5:
            return 5
        elif 5 <= self.opit <= 10:
            return 10
        else:
            return 15


if __name__ == "__main__":
    nn = Employee("Иван Иванов", "Разработчик", 3)
    ww = Employee("Анна Смирнова", "Менеджер", 7)
    ee = Employee("Пётр Петров", "Директор", 12)

    print(f"{nn.name}: бонус {nn.bonus()}%")
    print(f"{ww.name}: бонус {ww.bonus()}%")
    print(f"{ee.name}: бонус {ee.bonus()}%")

print("\nЗадание 3:")

from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def rest(self):
        pass



class Programmer(Worker):
    def work(self):
        return "Пишу код на Python"
    
    def rest(self):
        return "Сижу за пк"


class Teacher(Worker):
    def work(self):
        return "Играю в гта"
    
    def rest(self):
        return "Тралалело тралала"



programmer = Programmer()
teacher = Teacher()

print(programmer.rest())  
print(teacher.rest())    

print("\nЗадание 4:")
class Player:
    def __init__(self):
        self.xp = 0   # тут храним опыт игрока, пока 0

    def plus(self, x):
        # добавляем опыт 
        self.xp = self.xp + x

    def minus(self, x):
        # если хотят снять больше, чем есть — а вот НЕТ
        if x > self.xp:
            print("мало опыта, чел")
        else:
            # иначе просто уменьшаем
            self.xp = self.xp - x
# создаём игрока
p = Player()

# даём ему 100 опыта
p.plus(100)
print("xp =", p.xp)

# ещё 50 опыта, почему бы и нет
p.plus(50)
print("xp теперь =", p.xp)

# снимаем 30
p.minus(30)
print("после минуса =", p.xp)

# тут уже перебор, столько опыта нет
p.minus(200)
print("после попытки снять 200 =", p.xp)
