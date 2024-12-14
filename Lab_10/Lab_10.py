def sha1(message):
    def left_rotate(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

    # Ініціалізація змінних:
    h0, h1, h2, h3, h4 = (
        0x67452301,
        0xEFCDAB89,
        0x98BADCFE,
        0x10325476,
        0xC3D2E1F0,
    )

    # Попередня обробка:
    message = bytearray(message, "ascii")
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8

    # Додаємо біт '1' до повідомлення
    message.append(0x80)

    # Додаємо 0 <= k < 512 біт '0', щоб довжина повідомлення в бітах дорівнювала 448 (mod 512)
    while (len(message) * 8) % 512 != 448:
        message.append(0)

    # Додаємо початкову довжину повідомлення в бітах як 64-бітове число у форматі big-endian
    message += original_bit_len.to_bytes(8, byteorder="big")

    # Обробка повідомлення в послідовних 512-бітних блоках:
    for i in range(0, len(message), 64):
        w = [0] * 80
        chunk = message[i:i + 64]
        
        # Розбиваємо блок на шістнадцять 32-бітових слів у форматі big-endian
        for j in range(16):
            w[j] = int.from_bytes(chunk[j * 4:(j * 4) + 4], byteorder="big")

        # Розширюємо шістнадцять 32-бітових слів до вісімдесяти 32-бітових слів:
        for j in range(16, 80):
            w[j] = left_rotate((w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16]), 1)

        # Ініціалізація хеш-значення для цього блоку:
        a, b, c, d, e = h0, h1, h2, h3, h4

        # Основний цикл:
        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= j <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        # Додаємо хеш цього блоку до загального результату:
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    # Формуємо остаточне хеш-значення (big-endian) як 160-бітове число:
    return "".join(hex(x)[2:].rjust(8, "0") for x in (h0, h1, h2, h3, h4))

# Тестування функції SHA-1
test_message = input("Введіть повідомлення для хешування: ")
hash_value = sha1(test_message)
print(f"SHA-1 Хеш: {hash_value}")
