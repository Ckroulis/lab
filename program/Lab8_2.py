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


my_instance = MyClass("Бош", "Синий")
my_instance.set_size("Огромный")
my_instance.set_weight(10.5)

print(my_instance.get_size())
print(my_instance.get_weight())
