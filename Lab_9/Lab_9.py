import random
from math import gcd

def is_prime_rabin_miller(n, k=5):
    """Перевірка числа n на простоту тестом Рабіна-Міллера"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Представимо n-1 як 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Тестування
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

def generate_large_prime(bits=16):
    """Генерує просте число заданої довжини в бітах."""
    while True:
        p = random.getrandbits(bits)
        p |= (1 << bits - 1) | 1  # Забезпечуємо потрібну кількість біт і непарність
        if is_prime_rabin_miller(p):
            return p

def find_primitive_root(p):
    """Знаходить первісний корінь за модулем p."""
    if p == 2:
        return 1
    phi = p - 1
    factors = set()
    n = phi
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 1:
        factors.add(n)

    for g in range(2, p):
        if all(pow(g, phi // factor, p) != 1 for factor in factors):
            return g
    return None

def mod_inverse(a, p):
    """Обчислює мультиплікативний обернений елемент a за модулем p."""
    return pow(a, -1, p)

def elgamal_generate_keys(bits=16):
    """Генерує відкритий і закритий ключі для схеми Ель-Гамаля."""
    p = generate_large_prime(bits)
    g = find_primitive_root(p)
    x = random.randint(1, p - 2)  # Закритий ключ
    y = pow(g, x, p)  # Відкритий ключ
    return (p, g, y), x

def elgamal_encrypt(message, public_key):
    """Шифрує повідомлення message з використанням відкритого ключа."""
    p, g, y = public_key
    if message >= p:
        raise ValueError("Повідомлення має бути меншим за p.")
    k = random.randint(1, p - 2)  # Випадкове число
    c1 = pow(g, k, p)
    c2 = (message * pow(y, k, p)) % p
    return c1, c2

def elgamal_decrypt(ciphertext, private_key, public_key):
    """Розшифровує повідомлення з використанням закритого ключа."""
    c1, c2 = ciphertext
    p, g, y = public_key
    x = private_key
    s = pow(c1, x, p)  # c1^x % p
    s_inv = mod_inverse(s, p)  # Обернений елемент до s
    message = (c2 * s_inv) % p
    return message

# Тестування
public_key, private_key = elgamal_generate_keys(bits=16)
print("Публічний ключ:", public_key)
print("Приватний ключ:", private_key)

message = int(input("Введіть повідомлення (ціле число): "))
if message >= public_key[0]:
    print(f"Помилка: Повідомлення {message} має бути меншим за p ({public_key[0]}).")
else:
    ciphertext = elgamal_encrypt(message, public_key)
    print("Зашифроване повідомлення:", ciphertext)

    decrypted_message = elgamal_decrypt(ciphertext, private_key, public_key)
    print("Розшифроване повідомлення:", decrypted_message)
