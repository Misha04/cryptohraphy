# Вхідні дані
b = "101011"
n = 5

# Таблиця S-бокса 5
S5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
]

# Обчислення рядка і стовпця
row = int(b[0] + b[5], 2)
col = int(b[1:5], 2)

# Результат
output = S5[row][col]
binary_output = format(output, "04b")

print(f"Результат виходу: {output} (десяткове), {binary_output} (двійкове)")