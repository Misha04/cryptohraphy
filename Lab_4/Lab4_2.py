def gcdex(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def inverse_element(a, n):
    d, x, _ = gcdex(a, n)
    if d != 1:
        return None  # обернений елемент не існує, якщо НСД(a, n) != 1
    return x % n  # повертаємо x в межах модуля n

# Тестування функції на прикладі a = 5 і n = 18

a, n = 5, 18
print (f"a = {a}, n = {n}")
inverse = inverse_element(a, n)
print(f"Мультиплікативний обернений елемент {a} по модулю {n} дорівнює {inverse}")
