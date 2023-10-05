# Тема 4. Функции и стандартные модули/библиотеки
Отчет по Теме #4 выполнила:
- Куканова Мария Андреевна
- ЗПИЭ-20-2

| Задание | Сам_раб |
| ------ | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Дайте подробный комментарий для кода, написанного ниже. Комментарий нужен для каждой строчки кода, нужно описать что она делает. Не забудь те, что функции комментируются по-особенному.

```python
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
```

### Результат
![Меню](https://github.com/segamega-drive/software_engineering/blob/a3f08dc52d30e95b070be7adc0a2f6c6fc21ebf7/img/4.1.png)

## Выводы

  
## Самостоятельная работа №2
### Напишите программу, которая будет заменять игральную кость с 6 гранями. Если значение равно 5 или 6, то в консоль выводится «Вы победили», если значения 3 или 4, то вы рекурсивно должны вызвать эту же функцию, если значение 1 или 2, то в консоль выводится «Вы проиграли». При этом каждый вызов функции необходимо выводить в консоль значение “кубика”. Для выполнения задания необходимо использовать стандартную библиотеку random. Программу нужно написать, используя одну функцию и “точку входа”.

```python

```

### Результат
![Меню](https://github.com/segamega-drive/software_engineering/blob/161b639c23a3c971f4c0ad73cbb7ff2c1640bad4/img/4.2.png)

## Выводы

 
## Самостоятельная работа №3
### Напишите программу, которая будет выводить текущее время, с точностью до секунд на протяжении 5 секунд. Программу нужно написать с использованием цикла. Подсказка: необходимо использовать модуль datetime и time, а также вам необходимо как-то “усыплять” программу на 1 секунду.

```python

```

### Результат
![Меню](https://github.com/segamega-drive/software_engineering/blob/161b639c23a3c971f4c0ad73cbb7ff2c1640bad4/img/4.3.png)

## Выводы


## Самостоятельная работа №4
### Напишите программу, которая считает среднее арифметическое от аргументов вызываемое функции, с условием того, что изначальное количество этих аргументов неизвестно. Программу необходимо реализовать используя одну функцию и “точку входа”.

```python

```

### Результат
![Меню](https://github.com/segamega-drive/software_engineering/blob/161b639c23a3c971f4c0ad73cbb7ff2c1640bad4/img/4.4.1.png)
![Меню](https://github.com/segamega-drive/software_engineering/blob/161b639c23a3c971f4c0ad73cbb7ff2c1640bad4/img/4.4.2.png)

## Выводы

 
## Самостоятельная работа №5
### Создайте два Python файла, в одном будет выполняться вычисление площади треугольника при помощи формулы Герона (необходимо реализовать через функцию), а во втором будет происходить взаимодействие с пользователем (получение всей необходимой информации и вывод результатов). Напишите эту программу и выведите в консоль полученную площадь.

```python

```

### Результат
![Меню](https://github.com/segamega-drive/software_engineering/blob/161b639c23a3c971f4c0ad73cbb7ff2c1640bad4/img/4.5.png)

## Выводы


## Общие выводы по теме
