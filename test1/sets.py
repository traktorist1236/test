# name = {1, "2", 3.0, True, False}
# Множина не може зберігати дубльовані елементи
# Додати елемент, використовуємо .add(element)
# Прибрати елемент, використовуємо .discard(element)
# Щоб прінтити елементи, ми не можемо користуватись індексацією [], лише for циклом

mnozina = {1, 2, 2, 1, 1}
print(mnozina) # {1, 2} - дубльовані елементи прибрані
for element in mnozina:
    print(element)

# 1
# 2