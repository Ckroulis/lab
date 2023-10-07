# Тема 6. Базовые коллекции: словари, кортежи
Отчет по Теме #6 выполнил(а):
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
### При создании сайта у вас возникла потребность обрабатывать данные пользователя в странной форме, а потом переводить их в нужные вам форматы. Вы хотите принимать от пользователя последовательность чисел, разделенных пробелом, а после переформатировать эти данные в список и кортеж. Реализуйте вашу задумку. Для получения начальных данных используйте input(). Результатом программы будет выведенный список и кортеж из начальных данных.

```python
res = input().split()
y = tuple(res)
print(res)
print(y)
```

### Результат
![Меню](https://github.com/Ckroulis/lab/blob/Tema-6/pic/Lab6_1.jpg)

## Выводы
Научилась писать программу, которая позволяет обрабатывать данные пользователя в нестандартной форме и переводить их в нужные форматы.
  
## Самостоятельная работа №2
### Николай знает, что кортежи являются неизменяемыми, но он очень упрямый и всегда хочет доказать, что он прав. Студент решил создать функцию, которая будет удалять первое появление определенного элемента из кортежа по значению и возвращать кортеж без него. Попробуйте повторить шедевр не признающего авторитеты начинающего программиста. Но учтите, что Николай не всегда уверен в наличии элемента в кортеже (в этом случае кортеж вернется функцией в исходном виде).

```python
def virez(cort, a):
    if not (a in cort):
        return cort
    else:
        k = cort.index(a)
        return tuple(list(cort)[0:k] + list(cort[k + 1:]))


print(virez((8, 8, 3, 4, 2), 8))
```

### Результат
![Меню](https://github.com/Ckroulis/lab/blob/Tema-6/pic/Lab6_2.jpg)

## Выводы
Воспользоваласб хитростями и смогла "изменить" неизменяемый тип данных

## Самостоятельная работа №3
### Ребята поспорили кто из них одним нажатием на numpad наберет больше повторяющихся цифр, но не понимают, как узнать победителя. Вам им нужно в этом помочь. Дана строка в виде случайной последовательности чисел от 0 до 9 (длина строки минимум 15 символов). Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайте функцию, принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел, также эти значения нужно вывести в порядке возрастания ключа.

```python
def count_most_common_numbers(input_string):
    # Создаем словарь для подсчета количества каждой цифры
    count_dict = {}

    # Проходимся по каждой цифре в строке и увеличиваем ее счетчик в словаре
    for a in input_string:
        if a.isdigit():  # Проверяем, что символ является цифрой
            a = int(a)
            if a in count_dict:
                count_dict[a] += 1
            else:
                count_dict[a] = 1

    # Сортируем словарь по значениям в убывающем порядке и берем 3 самых частых числа
    sorted_counts = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    top_3_numbers = sorted_counts[:3]

    # Создаем словарь из топ-3 чисел в порядке возрастания ключей
    result_dict = {k: v for k, v in sorted(top_3_numbers)}

    return result_dict

# Получаем строку от пользователя
input_string = input("Введите последовательность цифр (минимум 15 символов): ")

# Проверяем, что длина введенной строки не меньше 15 символов
if len(input_string) < 15:
    print("Длина строки слишком мала.")
else:
    # Вызываем функцию и выводим результат
    result = count_most_common_numbers(input_string)
    print("Словарь с 3 самыми часто встречающимися числами (по убыванию):")
    print(result)
```

### Результат
![Меню](https://github.com/Ckroulis/lab/blob/Tema-6/pic/Lab6_3.jpg)

## Выводы

Научилась работать со словарями и снова повторила своиства строк

## Самостоятельная работа №4
### Ваш хороший друг владеет офисом со входом по электронным картам, ему нужно чтобы вы написали программу, которая показывала в каком порядке сотрудники входили и выходили из офиса. Определение сотрудника происходит по id. Напишите функцию, которая на вход принимает кортеж и случайный элемент (id), его можно придумать самостоятельно. Требуется вернуть новый кортеж, начинающийся с первого появления элемента в нем и заканчивающийся вторым его появлением включительно. Если элемента нет вовсе – вернуть пустой кортеж. Если элемент встречается только один раз, то вернуть кортеж, который начинается с него и идет до конца исходного.

```python
def get_employee_movement(log, employee_id):
    start_index = None
    end_index = None

    # Находим индексы первого и второго появления элемента
    for i, item in enumerate(log):
        if item == employee_id:
            if start_index is None:
                start_index = i
            else:
                end_index = i

    # Если элемент не найден, возвращаем пустой кортеж
    if start_index is None:
        return ()

    # Если второе появление элемента не найдено, возвращаем кортеж от первого появления до конца
    if end_index is None:
        return log[start_index:]

    # Возвращаем кортеж от первого до второго появления элемента включительно
    return log[start_index:end_index + 1]


log = (1, 2, 3, 4, 2, 3, 5, 4)
employee_id = 2
result = get_employee_movement(log, employee_id)
print(result)
```

### Результат
![Меню](https://github.com/Ckroulis/lab/blob/Tema-6/pic/Lab6_4.jpg)

## Выводы

Изучены методы работы с кортежами, такие как index() и создание подкортежа с помощью срезов.

## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, в которой будут обязательно использоваться кортеж или список. Проведите минимум три теста для проверки работоспособности вашей задачи.
### Перед студентом стоит задача: на вход функции sieve() поступает список целых чисел. В результате выполнения этой функции будет получен кортеж уникальных элементов списка в обратном порядке.

```python
def sieve(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.reverse()
    return tuple(unique_numbers)

numbers = [1, 2, 3, 4, 4, 5, 5, 6]
result = sieve(numbers)
print(result)
```

### Результат
![Меню](https://github.com/Ckroulis/lab/blob/Tema-6/pic/Lab6_5.jpg)

## Выводы
Узнала что функцию sieve() можно реализовать с помощью встроенных функций и методов Python, таких как set(), list() и reversed().

## Общие выводы по теме
В ходе работы выясняла, что кортежи и списки являются универсальными и гибкими структурами данных, позволяющими хранить и обрабатывать коллекции элементов.
Кортежи являются неизменяемыми, в то время как списки могут быть изменены. Это означает, что элементы кортежа не могут быть изменены после его создания, в отличие от списков.
