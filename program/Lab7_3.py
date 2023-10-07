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