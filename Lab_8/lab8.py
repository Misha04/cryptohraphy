import random

# Функція для перевірки числа на простоту за методом Міллера-Рабіна
def is_probable_prime(n, rounds):
    if n < 2 or n % 2 == 0:
        return False
    s = 0
    d = n - 1
    # Розкладаємо n-1 у вигляді d * 2^s
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(rounds):
        base = random.randint(2, n - 2)  # Випадкова база для перевірки
        x = pow(base, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)  # Квадрат числа (x^2 mod n)
            if x == n - 1:
                break
        else:
            return False  # Число складне
    return True  # Число просте

# Генеруємо велике безпечне просте число (safe prime)
def generate_large_safe_prime(bits, rounds=5):
    while True:
        # Генерація кандидата для перевірки
        potential_prime = random.getrandbits(bits - 1)
        potential_prime |= (1 << (bits - 2)) | 1  # Забезпечуємо потрібну довжину та непарність
        if is_probable_prime(potential_prime, rounds):
            safe_prime = 2 * potential_prime + 1  # Безпечне просте: 2p + 1
            if is_probable_prime(safe_prime, rounds):
                return safe_prime

# Знаходимо примітивний корінь модуля
def find_primitive_root(modulus):
    phi = modulus - 1  # Значення функції Ейлера
    while True:
        candidate = random.randint(2, modulus - 2)  # Кандидат для перевірки
        # Перевірка, чи є число примітивним коренем
        if pow(candidate, 2, modulus) != 1 and pow(candidate, phi // 2, modulus) != 1:
            return candidate

# Реалізація протоколу обміну ключами Діффі-Геллмана
def secure_key_exchange(bits=512):
    # Генеруємо просте число та примітивний корінь
    prime = generate_large_safe_prime(bits)
    generator = find_primitive_root(prime)
    print(f"Підходяще просте число: {prime}")
    print(f"Примітивний корінь: {generator}")

    # Алекс генерує свій особистий та публічний ключ
    alex_secret = random.randint(2, prime - 2)
    alex_public = pow(generator, alex_secret, prime)

    # Сем генерує свій особистий та публічний ключ
    sam_secret = random.randint(2, prime - 2)
    sam_public = pow(generator, sam_secret, prime)

    # Обчислення спільних ключів
    alex_shared = pow(sam_public, alex_secret, prime)
    sam_shared = pow(alex_public, sam_secret, prime)

    # Вивід ключів
    print(f"Особистий ключ Алекса: {alex_secret}")
    print(f"Публічний ключ Алекса: {alex_public}")
    print(f"Особистий ключ Сема: {sam_secret}")
    print(f"Публічний ключ Сема: {sam_public}")
    print(f"Спільний ключ Алекса: {alex_shared}")
    print(f"Спільний ключ Сема: {sam_shared}")
    print("Чи збігаються спільні ключі?", alex_shared == sam_shared)

secure_key_exchange(bits=64)
