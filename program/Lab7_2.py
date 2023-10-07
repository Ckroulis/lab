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
