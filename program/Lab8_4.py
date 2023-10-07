class MyClass:
    def __init__(self):
        self.public_attribute = "Публичный атрибут"
        self._protected_attribute = "Защищенный атрибут"
        self.__private_attribute = "Приватный атрибут"

    def public_method(self):
        print("Это публичный метод")

    def _protected_method(self):
        print("Это защищенный метод")

    def __private_method(self):
        print("Это приватный метод")

    def access_private_attribute(self):
        return self.__private_attribute

obj = MyClass()
print(obj.public_attribute)
print(obj._protected_attribute)
print(obj.access_private_attribute())

obj.public_method()
obj._protected_method()
obj._MyClass__private_method()

