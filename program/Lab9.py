# В классе Tomato создается статическое свойство states, которое содержит все стадии созревания помидора. В методе
# __init__() инициализируются два динамических свойства: _index (передается параметром) и _state (принимает первое
# значение из словаря states). Метод grow() переводит томат на следующую стадию созревания, если он не достиг
# последней стадии. Метод is_ripe() проверяет, что томат стал спелым.
class Tomato:
    states = {
        0: 'Отсутствует',
        1: 'Цветение',
        2: 'Зеленый',
        3: 'Красный'
    }

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < len(self.states) - 1:
            self._state += 1

    def is_ripe(self):
        return self._state == len(self.states) - 1


# Теперь создадим класс TomatoBush, который будет содержать список томатов: В методе __init__() класса TomatoBush
# создается список объектов класса Tomato на основе переданного количества помидоров. Метод grow_all() переводит все
# объекты в списке томатов на следующую стадию созревания. Метод all_are_ripe() возвращает True, если все томаты из
# списка стали спелыми. Метод give_away_all() очищает список томатов после сбора урожая.
class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(1, num_tomatoes + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


# Наконец, создадим класс Gardener: В методе __init__() класса Gardener определяются два динамических свойства: name
# (передается параметром) и _plant (принимает объект класса TomatoBush). Метод work() позволяет садовнику работать,
# что в свою очередь заставляет растение становиться более зрелым. Метод harvest() проверяет, все ли плоды созрели,
# и если да, то садовник собирает урожай, а иначе выводит предупреждение. Статический метод knowledge_base() выводит
# в консоль справку по садоводству.
class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран.")
        else:
            print("Не все плоды созрели. Продолжайте ухаживать за растением.")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")
        print("- Помидоры проходят несколько стадий созревания: отсутствие, цветение, зеленый, красный.")
        print("- Садовник может ухаживать за растением, собирать урожай и проверять зрелость плодов.")


Gardener.knowledge_base()

tomato_bush = TomatoBush(5)
gardener = Gardener("Иван", tomato_bush)

gardener.work()
gardener.work()
gardener.harvest()

gardener.work()
gardener.harvest()
