class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        pass


class Sparrow(Bird):
    def fly(self):
        return f"{self.name} летает в небе"


class Penguin(Bird):
    def fly(self):
        return f"{self.name} не может летать"


class Ostrich(Bird):
    def fly(self):
        return f"{self.name} тоже не умеет летать"


# Создаем экземпляры разных птиц
sparrow = Sparrow("Воробей")
penguin = Penguin("Пенгвин")
ostrich = Ostrich("Страус")

# Вызываем метод fly() для каждой птицы
print(sparrow.fly())
print(penguin.fly())
print(ostrich.fly())
