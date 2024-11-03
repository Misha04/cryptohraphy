def phi(m):
    result = m
    p = 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            result -= result // p
        p += 1
    if m > 1:
        result -= result // m
    return result

def inverse_element_2(a, n):
    if gcd(a, n) != 1:
        return None  # обернений елемент не існує, якщо a та n не є взаємно простими
    phi_n = phi(n)
    return pow(a, phi_n - 1, n)  # обчислення a^(phi(n)-1) % n

# Додаткова функція для обчислення НСД
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# Тестування функції на прикладі a = 5 і n = 18
a, n = 5, 18
inverse = inverse_element_2(a, n)
print(f"Мультиплікативний обернений елемент {a} по модулю {n} дорівнює {inverse}")
