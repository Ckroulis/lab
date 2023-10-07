def sum_with_input(num1):
    try:
        num2 = float(input("Введите число: "))  # Ввод числа, преобразованного в тип float
        result = num1 + num2
        print("Результат:", result)
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")


sum_with_input(2)
