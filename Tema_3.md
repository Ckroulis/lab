# Тема 2. Базовые операции языка Python
Отчет по Теме #2 выполнила:
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
### Напишите программу, которая преобразует 1 в 31. Для выполнения поставленной задачи необходимо обязательно и только один раз использовать: Цикл for *= 5 += 1 Никаких других действий или циклов использовать нельзя.

```python
a = 1
for a in range(7):
    a *= 5
a += 1
print(a)
```
### Результат.
![Меню](https://github.com/Ckroulis/lab/blob/Tema-2/pic/lab2_1.jpg)

## Выводы

В данном коде выводятся одна строка с использованием функции `print()` и в самом начале объявляется переменная для сравнения. Каждая строка содержит разные значения:

1. `att = 5`: Переменной присваиваем значение `5`.

2. `print(att == 0)`: Выводится результат сравнения `att == 0`. Выводится в консоль `False`.