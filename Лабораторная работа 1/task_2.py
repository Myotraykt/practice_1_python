# Параметры книги
pages = 100  # количество страниц
lines_per_page = 50  # число строк на странице
chars_per_line = 25  # количество символов в строке
bytes_per_char = 4  # байты для хранения одного символа

# Объем одной книги в байтах
book_size = pages * lines_per_page * chars_per_line * bytes_per_char

# Объем дискеты в байтах (1,44 Мб)
disk_size_mb = 1.44
disk_size_bytes = int(disk_size_mb * 1024 * 1024)  # Приводим к целочисленному типу

# Количество книг, которые можно поместить на дискету
number_of_books = disk_size_bytes // book_size  # Используем целочисленное деление

# Вывод результата
print("Количество книг, помещающихся на дискету:", number_of_books)
