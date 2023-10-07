class MyClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")


# Создание объекта класса MyClass
obj = MyClass("Maria")

# Вызов метода say_hello объекта obj
obj.say_hello()