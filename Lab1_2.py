def caesar_cipher_with_keyword(text, keyword, k, alphabet="АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"):
    # 1. Очищуємо ключове слово від повторюваних символів, зберігаючи порядок
    cleaned_keyword = ""
    for letter in keyword:
        if letter not in cleaned_keyword:
            cleaned_keyword += letter

    # 2. Створюємо початкову частину шифрувального алфавіту з очищеного ключового слова
    cipher_alphabet = cleaned_keyword

    # 3. Додаємо решту літер алфавіту після зміщення на k, уникаючи повторів
    remaining_alphabet = alphabet[k:] + alphabet[:k]
    for letter in remaining_alphabet:
        if letter not in cipher_alphabet:
            cipher_alphabet += letter

    # Виведення шифрувального алфавіту
    print("Шифрувальний алфавіт:", cipher_alphabet)

    # 4. Шифруємо текст і виводимо кожен крок
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            encrypted_letter = cipher_alphabet[index]
            print(f"Шифруємо '{letter}' як '{encrypted_letter}'")  # Вивід шифрування кожної літери
            encrypted_text += encrypted_letter
        else:
            encrypted_text += letter  # Якщо символ не в алфавіті, додаємо його без змін

    return encrypted_text

# Вхідні дані
text = "ВОГОНЬ"
keyword = "ВОДА"
k = 3

print("Початковий текст: ", text)
print("Ключове слово: ", keyword)
print("Число k для зміщення алфавіту: ", k)

# Виконання шифрування
encrypted_text = caesar_cipher_with_keyword(text, keyword, k)
print("Зашифрований текст:", encrypted_text)
