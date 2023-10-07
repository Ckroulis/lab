try:
    with open("Пустой файл.txt", "r") as file:
        data = file.read()
        if len(data) == 0:
            raise Exception("файл пустой")
        else:
            print(data)
except FileNotFoundError:
    print("Файл не найден")
except Exception as e:
    print(str(e))

try:
    with open("Не пустой файл.txt", "r") as file:
        data = file.read()
        if len(data) == 0:
            raise Exception("файл пустой")
        else:
            print(data)
except FileNotFoundError:
    print("Файл не найден")
except Exception as e:
    print(str(e))