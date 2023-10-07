class MyClass:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.size = None
        self.weight = None

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

class MyChildClass(MyClass):
    def __init__(self, arg1, arg2, arg3):
        super().__init__(arg1, arg2)  # Вызываем конструктор родительского класса
        self.arg3 = arg3

    def method3(self):
        # Добавляем новый метод в дочерний класс
        print("Method 3")
    def method2(self):
        # Добавляем новый метод в дочерний класс
        print("Method 2")
    def method1(self):
        # Добавляем новый метод в дочерний класс
        print("Method 1")

# Пример использования
instance = MyChildClass("Arg 1", "Arg 2", "Arg 3")
instance.method1()  # Вызываем метод родительского класса
instance.method2()  # Вызываем метод родительского класса
instance.method3()  # Вызываем метод дочернего класса

my_instance = MyClass("Бош", "Синий")
my_instance.set_size("Огромный")
my_instance.set_weight(10.5)

print(my_instance.get_size())
print(my_instance.get_weight())
