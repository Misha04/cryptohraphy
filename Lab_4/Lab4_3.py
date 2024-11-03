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


m = int(input("Введіть значення m "))
phi_value = phi(m)
print(f"Значення функції Ейлера для {m} дорівнює {phi_value}")
