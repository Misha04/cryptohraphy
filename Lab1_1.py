# Визначаємо матрицю і розміщуємо текст
text = "програмнезабезпечення"
column_key = "крипто"
row_key = "шифр"

# Встановлюємо розмірність матриці (4x6 у цьому випадку)
rows, columns = 4, 6
matrix = [[''] * columns for _ in range(rows)]

# Заповнюємо матрицю по рядках
index = 0
for i in range(rows):
    for j in range(columns):
        if index < len(text):
            matrix[i][j] = text[index]
            index += 1

# Перестановка стовпців за стовпцевим ключем
sorted_column_key = sorted([(char, ind) for ind, char in enumerate(column_key)])
column_order = [ind for _, ind in sorted_column_key]

# Застосовуємо перестановку стовпців
matrix_with_reordered_columns = [[row[column_order[j]] for j in range(columns)] for row in matrix]

# Додаємо рядковий ключ до матриці і переставляємо рядки
matrix_with_row_key = [[row_key[i]] + matrix_with_reordered_columns[i] for i in range(rows)]

# Сортуємо рядки за рядковим ключем
sorted_row_key = sorted([(char, ind) for ind, char in enumerate(row_key)])
row_order = [ind for _, ind in sorted_row_key]

# Застосовуємо перестановку рядків
final_matrix = [matrix_with_row_key[row_order[i]] for i in range(rows)]

# Отримуємо шифротекст, зчитуючи матрицю стовпець за стовпцем з врахуванням відступів
ciphertext = ''
counter = 0
for j in range(1, columns + 1):  # пропускаємо стовпець з рядковим ключем
    for i in range(rows):
        ciphertext += final_matrix[i][j]
        counter += 1
        # Додаємо пробіл після кожних 4 символів
        if counter % 4 == 0 and counter < rows * columns:
            ciphertext += ' '

print("Початковий текст: ", text)
print("Стовпцевий ключ: ", column_key)
print("Рядковий ключ: ", row_key)
# Виводимо кінцевий шифротекст
print("Шифротекст:", ciphertext)
