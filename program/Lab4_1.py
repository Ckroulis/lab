# подклчение библиотек datetime и math для исползования функций datetime и sqrt
from datetime import datetime
from math import sqrt


def main(**kwargs):
    '''
    Вычисляет длину гипотенузы по теореме Пифагора
    :param kwargs: Принимает переменное количество аргументов
    :return: Возвращает None, выводит результат вычислений
    '''
    for key in kwargs.items():
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        print(result)


# Прямой запуск если не было другого вызова
if __name__ == '__main__':
  # Переменная с датой и временем запуска функции
    start_time = datetime.now()
  # Вызов функции, в параметры передается список из двух переменных
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15])

# Вычисление время выполнения программы вычитая время начала работы программы из время начала выполнения программы
time_costs = datetime.now() - start_time

# Вывод времени выполнения программы
print(f"Время выполнения программы {time_costs}")