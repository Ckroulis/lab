import random

# Открываем файл на запись
with open('random.txt', 'w') as file:
    # Генерируем 25 случайных чисел
    for _ in range(25):
        # Генерируем случайное число от 1 до 10
        random_number = random.randint(1, 10)
        # Записываем число в файл
        file.write(str(random_number) + ' ')
