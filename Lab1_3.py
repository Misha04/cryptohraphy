correspondence_table = {
    'А': [17, 31, 48],
    'Б': [23, 44, 63],
    'В': [14, 89, 42],
    'Г': [55, 52, 11],
    'Ґ': [8, 36, 21],   
    'Д': [37, 88, 25],
    'Е': [97, 51, 15],
    'Є': [9, 12, 27],   
    'Ж': [47, 67, 33],
    'З': [76, 19, 59],
    'И': [27, 64, 73],
    'І': [5, 20, 85],  
    'Ї': [82, 54, 90], 
    'Й': [26, 68, 3],  
    'К': [77, 38, 45],
    'Л': [22, 70, 90],
    'М': [12, 65, 84],
    'Н': [34, 28, 71],
    'О': [10, 40, 57],
    'П': [39, 49, 82],
    'Р': [91, 72, 60],
    'С': [26, 66, 54],
    'Т': [99, 18, 58],
    'У': [83, 29, 50],
    'Ф': [81, 94, 24],
    'Х': [92, 96, 36],
    'Ц': [20, 30, 62],
    'Ч': [13, 46, 75],
    'Ш': [35, 68, 80],
    'Щ': [100, 5, 3],
    'Ь': [1, 4, 2],
    'Ю': [8, 6, 9],
    'Я': [74, 95, 86]
}

# Індекс для доступу до наступного значення в таблиці відповідностей для кожної літери
counters = {letter: 0 for letter in correspondence_table}

def homophonic_encryption(text):
    encrypted_text = ""
    for letter in text:
        if letter in correspondence_table:
            # Отримуємо поточний індекс для вибору з таблиці відповідностей
            index = counters[letter]
            cipher = correspondence_table[letter][index]
            
            # Додаємо шифроване значення до результату
            encrypted_text += str(cipher)
            
            # Оновлюємо індекс для наступного використання цієї літери
            counters[letter] = (index + 1) % len(correspondence_table[letter])
        else:
            # Якщо символ не в таблиці, додаємо його без змін
            encrypted_text += letter
    return encrypted_text

# Тестовий приклад
text = "ЖАЖДА"
print("Початковий текст: ", text)
encrypted_text = homophonic_encryption(text)
print("Зашифрований текст:", encrypted_text)
