import random

def is_prime(n, k=128):
    """Перевірка простоти числа n за допомогою тесту Міллера — Рабіна."""
    if n <= 1:
        return False, 0
    if n <= 3:
        return True, 1  # 2 і 3 - прості числа
    if n % 2 == 0:
        return False, 0

    # Представимо n-1 як d * 2^r
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Тестування k разів
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # a^d % n
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False, 1  # Складене число

    # Ймовірність простоти
    probability = 1 - (1 / (4 ** k))
    return True, probability

# Введення даних
p = int(input("Введіть непарне натуральне число p > 3: "))
k = int(input("Введіть кількість раундів k: "))

# Перевірка простоти
result, probability = is_prime(p, k)

# Виведення результату
if result:
    print(f"{p} - просте число з ймовірністю {probability:.6f}.")
else:
    print(f"{p} - складене число.")
