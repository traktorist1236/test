# назва_змінної = значення_змінної
# for назва_ітерації in range(кількість): - кількість тип: int
# while умова: (f.e. while index<=1: ...)

loop = int(input("Скільки разів повторити: "))
for i in range(loop):
    print(f"test {i+1}")

i = 0
while i<10:
    print(i+1)
    i += 1
    
# ===========================================================

# Прінт всіх елементів списку або кортежу
# for element_name in list_or_tuple_name: ...

array = [1, 2, 3, 4, 5]
test_tupple = (1, 2, 3, 4, 5)

for element in array:
    print(element)

for element in test_tupple:
    print(element)