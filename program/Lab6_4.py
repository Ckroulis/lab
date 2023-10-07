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
