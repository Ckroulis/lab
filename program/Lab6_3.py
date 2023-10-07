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