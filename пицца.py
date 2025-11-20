from abc import ABC, abstractmethod

# Базовые классы
class Pizza(ABC):
    def __init__(self, name, price):
        self.name, self.price = name, price
    
    @abstractmethod
    def get_price(self):
        pass  # Абстрактный метод — должен быть реализован в наследниках

class Ingredient:
    def __init__(self, name, price):
        self.name, self.price = name, price
    
    def get_price(self):
        return self.price  # Возвращает цену ингредиента

# Конкретные пиццы (наследники абстрактного класса Pizza)
class Margarita(Pizza):
    def __init__(self):
        super().__init__("Маргарита", 15.0)  # Название и цена пиццы
    
    def get_price(self):
        return self.price  # Возвращает сохранённую цену

class Pepperoni(Pizza):
    def __init__(self):
        super().__init__("Пепперони", 12.5)
    
    def get_price(self):
        return self.price

class FourCheeses(Pizza):
    def __init__(self):
        super().__init__("Четыре сыра", 14.0)
    
    def get_price(self):
        return self.price

# Сервис для управления заказом
class OrderManager:
    def create(self, balance):
        # Создаёт новый заказ с начальным балансом
        return {"pizza": None, "ings": [], "total": 0.0, "balance": balance}
    

    def set_pizza(self, order, pizza):
        # Проверяет, хватает ли денег на пиццу
        if order["balance"] >= pizza.get_price():
            order["pizza"] = pizza  # Сохраняет выбранную пиццу
            order["balance"] -= pizza.get_price()  # Списывает стоимость
            order["total"] += pizza.get_price()  # Увеличивает итоговую сумму
            return True  # Успех
        return False  # Не хватило денег

    def add_ing(self, order, ing):
        # Проверяет лимит ингредиентов (не более 3)
        if len(order["ings"]) >= 3:
            print("Максимум 3 ингредиента!")
            return False
        
        # Проверяет, хватает ли денег на ингредиент
        if order["balance"] >= ing.get_price():
            order["ings"].append(ing)  # Добавляет ингредиент в заказ
            order["balance"] -= ing.get_price()  # Списывает стоимость
            order["total"] += ing.get_price()  # Увеличивает итоговую сумму
            return True  # Успех
        return False  # Не хватило денег

# Сервис для расчёта итоговой стоимости
class PriceCalculator:
    def calculate(self, pizza, ings):
        # Сумма: цена пиццы + цены всех ингредиентов
        return pizza.get_price() + sum(i.get_price() for i in ings)

# Сервис для вывода чека
class ReceiptPrinter:
    def print(self, order):
        print(f"\n{'='*30}")
        print("ВАШ ЗАКАЗ")
        print("="*30)
        print(f"Пицца: {order['pizza'].name}")
        print(f"Цена пиццы: {order['pizza'].get_price():.2f} руб.")
        
        if order["ings"]:  # Если есть ингредиенты
            print("\nДополнительные ингредиенты:")
            for i, ing in enumerate(order["ings"], 1):
                print(f"{i}. {ing.name} — {ing.get_price():.2f} руб.")
        
        
        print("-"*30)
        print(f"Итого: {order['total']:.2f} руб.")
        print(f"Остаток на счету: {order['balance']:.2f} руб.")
        print("="*30)

# Основное приложение
class PizzaApp:
    def __init__(self):
        self.order_mgr = OrderManager()  # Менеджер заказов
        self.price_calc = PriceCalculator()  # Калькулятор цены
        self.receipt_printer = ReceiptPrinter()  # Печать чека
        # Список доступных пицц
        self.pizzas = [Margarita(), Pepperoni(), FourCheeses()]
        # Список доступных ингредиентов
        self.ings = [
            Ingredient("Грибы", 10.0),
            Ingredient("Оливки", 8.5),
            Ingredient("Курица", 15.0),
            Ingredient("Ананасы", 2.5)
        ]
        self.initial_balance = 30.0  # Начальный баланс пользователя

    def show_menu(self):
        # Выводит меню с балансом, пиццами и ингредиентами
        print(f"\n💵 Ваш баланс: {self.initial_balance:.2f} руб.")
        print("\n🍕 МЕНЮ ПИЦЦ")
        for i, p in enumerate(self.pizzas, 1):
            print(f"{i}. {p.name} — {p.get_price():.2f} руб.")
        
        print("\n🧀 ДОПОЛНИТЕЛЬНЫЕ ИНГРЕДИЕНТЫ (максимум 3)")
        for i, ing in enumerate(self.ings, 1):
            print(f"{i}. {ing.name} — {ing.get_price():.2f} руб.")


    def get_choice(self, prompt, options_count):
        # Бесконечный цикл для корректного ввода
        while True:
            try:
                choice = int(input(prompt))  # Преобразует ввод в число
                if choice == 0:
                    return 0  # Выход
                if 1 <= choice <= options_count:
                    return choice  # Верный выбор
                else:
                    print("Нет такого пункта. Попробуйте снова.")
            except ValueError:
                print("Введите число.")  # Если введено не число

    def run(self):
        # Приветственное сообщение
        print("\n\n\nПосле рабочего дня, Тарас шел по ночному городу, он обанкротился, в его кармане лежали несчастные 30р и единственное,\nчто он хотел - это поесть пиццы.\nЗайдя в помещение ему сказали: Добро пожаловать в пиццерию! 🍕")
        
        order = self.order_mgr.create(self.initial_balance)  # Создаём заказ
        
        # Выбор пиццы
        self.show_menu()
        pizza_choice = self.get_choice("\nВыберите пиццу (0 — выход): ", len(self.pizzas))
        if pizza_choice == 0:
            print("До свидания!")
            return
        
        selected_pizza = self.pizzas[pizza_choice - 1]
        if not self.order_mgr.set_pizza(order, selected_pizza):
            print("Недостаточно средств для покупки пиццы!")
            return
        
        print(f"Вы выбрали: {selected_pizza.name}")
        print(f"Списано: {selected_pizza.get_price():.2f} руб.")
        print(f"Остаток: {order['balance']:.2f} руб.\n")
        
        # Добавление ингредиентов
        print("Добавляйте ингредиенты (0 — завершить заказ):")
        while len(order["ings"]) < 3:
            ing_choice = self.get_choice("Номер ингредиента (0 для завершения): ", len(self.ings))
            if ing_choice == 0:
                break
            
            selected_ing = self.ings[ing_choice - 1]
            if not self.order_mgr.add_ing(order, selected_ing):
                print("Недостаточно средств для добавления ингредиента!")
                continue
            
            print(f"Добавили: {selected_ing.name}")
            print(f"Списано: {selected_ing.get_price():.2f} руб.")
            print(f"Остаток: {order['balance']:.2f} руб.\n")
        
        
        # Печать финального чека
        self.receipt_printer.print(order)
        print("\nСпасибо за заказ# Приятного аппетита!")

# Запуск приложения
if __name__ == "__main__":
    app = PizzaApp()
    app.run()
