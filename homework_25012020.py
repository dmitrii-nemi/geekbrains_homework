# Задание 1
my_list = (256, 'abc', ['a', 'b', 'c'], 2.5, None, ('h', 'e', 'l', 'l', 'o'))
for i in my_list:
    print(type(i))

# Задание 2
initial_list = list(input('Введите любые значения через пробел: ').split())
print(initial_list)
j = 0
for i in range(len(initial_list) // 2):
    initial_list[j], initial_list[j + 1] = initial_list[j + 1], initial_list[j]
    j += 2
print(initial_list)

# Задание 3
month = input('Введите номер месяца: ')
my_dict = {'1': 'зима',
           '2': 'зима',
           '3': 'весна',
           '4': 'весна',
           '5': 'весна',
           '6': 'лето',
           '7': 'лето',
           '8': 'лето',
           '9': 'осень',
           '10': 'осень',
           '11': 'осень',
           '12': 'зима',
           }
print(my_dict.get(month))

# Задание 4
line = input('Введите несколько слов, разделенных пробелами: ')
count = 1
for i in line.split():
    print('{}. {}'.format(count, i[0:10])) #не могу понять, почему пришлось делать срез до 10, а не 9 символа, но работает
    count += 1

# Задание 5
my_list = [7, 5, 3, 3, 2]
request = input('Введите число: ')
for index, number in enumerate(my_list):
    if int(request) <= int(my_list[index]):
        continue
    my_list.insert(index, request) # НЕ приведено к int чтобы было наглядно видно, куда вставляется введенное значение
    print(my_list)
    break
else:
    my_list.append(request)
    print(my_list)

# Задание 6
goods = []
while input("Хотите добавить товар? Введите Да/Нет: ") == 'Да':
    number = int(input("Введите номер продукта: "))
    features = {}
    while input("Хотите добавить характеристики товара? Введите Да/Нет: ") == 'Да':
        feature_key = input("Введите характеристику товара: ")
        feature_value = input("Введите значение характеристики товара: ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
    print(goods)
analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
            analitics[feature_key] = [feature_value]
            print(analitics)
