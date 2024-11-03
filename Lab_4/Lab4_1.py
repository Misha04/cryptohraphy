def gcdex(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

# Тестування функції на прикладі a = 612 і b = 342
a, b = 612, 342
d, x, y = gcdex(a, b)
print (f"a = {a}, b = {b}")
print(f"НСД: {d}, x: {x}, y: {y}")
print(f"Перевірка: {a} * {x} + {b} * {y} = {d}")
