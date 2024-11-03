import random

def is_prime(n, k=128):  # k - кількість раундів тесту
    """Перевірка простоти числа n за допомогою тесту Міллера — Рабіна."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

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
            return False
    return True

def generate_large_prime(bits):
    """Генерація великого простого числа заданої довжини в бітах."""
    while True:
        # Генеруємо випадкове число
        num = random.getrandbits(bits) | (1 << (bits - 1)) | 1  # Встановлюємо старший біт і останній
        if is_prime(num):
            return num

def gcd_extended(a, b):
    """Розширений алгоритм Евкліда для знаходження d."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    """Обчислення оберненого елемента по модулю phi."""
    gcd, x, _ = gcd_extended(e, phi)
    if gcd != 1:
        raise Exception('Обернений елемент не існує')
    else:
        return x % phi

def generate_rsa_keys(bits=1024):
    """Генерація відкритого та закритого ключів RSA."""
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    
    n = p * q
    phi = (p - 1) * (q - 1)

    # Вибір e
    e = 65537  # Зазвичай обирають 65537, оскільки це просте і має хороші властивості

    # Обчислення d
    d = mod_inverse(e, phi)

    # Повертаємо відкритий і закритий ключі
    return (e, n), (d, n)  # (відкритий ключ (e, n), закритий ключ (d, n))

# Генерація ключів RSA
public_key, private_key = generate_rsa_keys(1024)
print(f"Відкритий ключ: {public_key} \n")
print(f"Закритий ключ: {private_key}")
