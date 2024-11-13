numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Находим сумму всех элементов, исключая None
total_sum = sum(num for num in numbers if num is not None)

# Подсчитываем количество элементов, включая None
count = len(numbers)

# Рассчитываем среднее арифметическое
average = total_sum / (count)  # Убираем 1 для исключения None из расчёта

# Заменяем None на среднее арифметическое
numbers[numbers.index(None)] = average

# Выводим измененный список
print("Измененный список:", numbers)
