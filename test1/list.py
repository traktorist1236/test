# створення списку: name = [1, "2", 3.0, True, False, ...] 
# отримати елемент по його розміщенні: name[порядковий_номер] || Починаючи з 0
# додати елемент до кінця списку: name.append(значення) 
# забрати елемент по його назві: name.remove(значення)
# забрати останній елемент списку: name.pop()

# len(name) - повертає кількість елементів в списку

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(array[0]) # 1
print(array[9]) # 10
print(array[10]) # Error: list index out of range

print(array) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array.append(11)

print(array) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
array.remove(11)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

array.pop()
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]