# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил(а):
- Куканова Мария Андреевна
- ЗПИЭ-20-2

| Задание | Сам_раб |
| ------  | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class MyClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")


# Создание объекта класса MyClass
obj = MyClass("Maria")

# Вызов метода say_hello объекта obj
obj.say_hello()
```

### Результат
![Меню](https://github.com/Ckroulis/lab/blob/Tema-8/pic/Lab8_1.jpg)

## Выводы
С помощью классов можно создавать более сложные структуры данных, а также реализовывать наследование, полиморфизм и другие принципы ООП. Понимание создания классов является важным шагом в изучении программирования и позволяет создавать более модульный и гибкий код.

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```

### Результат
![Меню](https://github.com/Ckroulis/lab/blob/Tema-8/pic/Lab8_2.jpg)

## Выводы
Научилась создавать классы, добавлять им атрибуты и методы, а также создавать экземпляры класса и работать с ними.
  
## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```

### Результат
![Меню](https://github.com/Ckroulis/lab/blob/Tema-8/pic/Lab8_3.jpg)

## Выводы
Научилась реализовывать наследование, продолжая работать с ранее созданным классом.

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```

### Результат
![Меню](https://github.com/Ckroulis/lab/blob/Tema-8/pic/Lab8_4.jpg)

## Выводы
Научилась работать с концепции инкапсуляции, которая позволяет ограничить доступ к определенным методам и переменным внутри класса. Приватные методы и атрибуты обозначаются перед их именами с использованием подчеркивания. Одиночное подчеркивание указывает на доступ только внутри класса и его подклассов, а двойное подчеркивание обозначает доступ только внутри самого класса.

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```

### Результат
![Меню](https://github.com/Ckroulis/lab/blob/Tema-8/pic/Lab8_5.jpg)

## Выводы
Когда метод fly() вызывается для объекта Sparrow, Penguin или Ostrich, Python автоматически использует версию метода, присутствующую в соответствующем классе. То есть, метод "fly" запускается в контексте конкретного экземпляра класса и опирается на данные конкретного объекта (в данном случае - на имя объекта, которое используется для формирования вывода метода).

## Общие выводы по теме
В процессе изучения основ ООП мы осветили следующие концепции: классы, объекты, наследование, инкапсуляцию, полиморфизм и методы. Классы представляют собой шаблоны для создания объектов, в то время как объекты - это конкретные экземпляры классов. Наследование позволяет создавать новые классы на основе уже существующих, а инкапсуляция скрывает детали реализации класса. Полиморфизм позволяет использовать объекты разных классов в качестве объектов одного и того же типа.

