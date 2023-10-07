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