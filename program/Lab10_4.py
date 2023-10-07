import time

# Создаем класс декоратора CatDecorator
class CatDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()

        result = self.func(*args, **kwargs)

        execution_time = time.time() - start_time

        print(f"Функция '{self.func.__name__}' выполнилась за {execution_time} секунд.")

        return result

# Функция, которая выводит приветствие с именем кошки
@CatDecorator
def greet_cat(name):
    print(f"Привет, {name}! Мур-мур-мур!")

# Функция, которая складывает два числа с небольшой задержкой
@CatDecorator
def add_with_delay(a, b):
    time.sleep(2)
    return a + b


greet_cat("Кисыч")
result = add_with_delay(3, 5)
print(f"Результат сложения: {result}")
