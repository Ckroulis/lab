# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил(а):
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
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

```python
import re
from collections import Counter


with open('Статья.txt', 'r') as file:
    content = file.read()
    content = re.sub(r'[^\w\s]', '', content.lower())
    words = content.split()
    word_count = len(words)

    word_frequency = Counter(words)
    most_common_word = word_frequency.most_common(1)[0][0]

# Выводим результаты
print(f"Количество слов в файле: {word_count}")
print(f"Самое часто встречающееся слово: {most_common_word}")


with open('результат.txt', 'w') as result_file:
    result_file.write(f"Количество слов в файле: {word_count}\n")
    result_file.write(f"Самое часто встречающееся слово: {most_common_word}\n")
```

### Результат
![Меню](https://github.com/Ckroulis/lab/blob/Tema-7/pic/Lab7_1.1.jpg)
![Меню](https://github.com/Ckroulis/lab/blob/Tema-7/pic/Lab7_1.2.jpg)

## Выводы
Узнала, как открыть файл для чтения ('r') или записи ('w') с помощью функции open(). Метод read() использовала для чтения содержимого файла и метод 'write()' для записи в файл.
  
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
import csv

def create_expense():
    amount = input("Введите сумму расхода: ")
    category = input("Введите категорию расхода: ")
    description = input("Введите описание расхода: ")
    return [amount, category, description]

def save_expense(expense):
    with open('Расходы.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(expense)
    print("Расход успешно сохранен.")

def show_expenses():
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def main():
    while True:
        print("Выберите действие:")
        print("1. Ввести новый расход")
        print("2. Показать существующие расходы")
        print("3. Выйти")
        choice = input("Введите номер действия: ")

        if choice == '1':
            expense = create_expense()
            save_expense(expense)
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

if __name__ == '__main__':
    main()
```

### Результат
![Меню](https://github.com/Ckroulis/lab/blob/Tema-7/pic/Lab7_2.1.jpg)
![Меню](https://github.com/Ckroulis/lab/blob/Tema-7/pic/Lab7_2.2.jpg)

## Выводы
В данном задании научилась работать с csv-файлами, читать из них данные и производить в них запись. Из модуля csv классы DictWriter и DictReader позволяют работать с данными в формате словаря. Цикл while может иметь в условии булевый тип данных.
  
## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.

```python
def count_letters(text):
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
    return count


def count_words(text):
    words = text.split()
    return len(words)


def count_lines(text):
    lines = text.split('\n')
    return len(lines)


# Открываем файл и считываем его содержимое
with open('input.txt', 'r') as file:
    content = file.read()

# Вычисляем статистику
letter_count = count_letters(content)
word_count = count_words(content)
line_count = count_lines(content)

# Выводим результаты
print(f"Количество букв: {letter_count}")
print(f"Количество слов: {word_count}")
print(f"Количество строк: {line_count}")
```

### Результат
![Меню](https://github.com/Ckroulis/lab/blob/Tema-7/pic/Lab7_3.jpg)

## Выводы
В данном задании мы используем функцию match() из модуля re, проверяя с помощью регулярного выражения является ли каждый символ в строке буквой латинского алфавита, если да, то добавляем единицу к числу букв.

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.

```python
def replace_words(sentence, forbidden_words):
    words = sentence.lower().split()
    for forbidden_word in forbidden_words:
        lower_forbidden_word = forbidden_word.lower()
        sentence = sentence.replace(forbidden_word, '*' * len(lower_forbidden_word))
    return sentence

with open('input1.txt', 'r') as file:
    forbidden_words = file.read().split()

input_sentence = input('Введите предложение: ')
result = replace_words(input_sentence, forbidden_words)
print('Результат:', result)
```

### Результат
![Меню](https://github.com/Ckroulis/lab/blob/Tema-7/pic/Lab7_4.jpg)

## Выводы
Программа умеет открывать и читать файлы, используя контекстный менеджер (with open()) для обеспечения корректного закрытия файлов после завершения работы с ними, что является хорошей практикой. В данном случае файл читается целиком и разделяется на отдельные строки методом read().split().


## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.
### Программа должна создать файл с именем random.txt и записать в него случайные числа от 1 до 10 в количестве 25 штук.

```python
import random

# Открываем файл на запись
with open('random.txt', 'w') as file:
    # Генерируем 25 случайных чисел
    for _ in range(25):
        # Генерируем случайное число от 1 до 10
        random_number = random.randint(1, 10)
        # Записываем число в файл
        file.write(str(random_number) + ' ')
```

### Результат
![Меню](https://github.com/Ckroulis/lab/blob/Tema-7/pic/Lab7_5.jpg)

## Выводы
В данном задании происходит открытие файла в режиме записи. Также используется функция randint() для генерации случайного числа в диапазоне от 1 до 10 (верхняя граница диапазона считается). Происходит запись строк в файл с помощью метода writelines().

## Общие выводы по теме
Работа с файлами может быть полезной для хранения и сохранения данных програм, а также для обмена данными между разными програмами. Правильное понимание и использование функций и методов работы с файлами помогает создавать более гибкие и функциональные программы.
