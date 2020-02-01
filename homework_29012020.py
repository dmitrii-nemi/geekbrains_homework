# Задание 1
def my_dev_func(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return 'На 0 делить нельзя, введите другое значение y!'


print(my_dev_func(int(input('Введите x: ')), int(input('Введите y: '))))

# Задание 2
def user_data(name, surname, year_of_birth, home_town, email, phone_number):
    print(name, surname, year_of_birth, home_town, email, phone_number)


user_data(name='Александр', surname='Пушкин', year_of_birth='1799', home_town='Москва',
          email='apyshkin@gmail.com', phone_number='880090086875')

# Задание 3
def sum_of_two(x, y, z):
    list_of_num = [x, y, z]
    list_of_num.sort()
    print(list_of_num[1] + list_of_num[2])


sum_of_two(-4, -8, -6)

# Задание 4
# 1
def my_func(x, y):
    return x ** abs(y)


print(my_func(5, -3))

# 2
def my_func(x, y, z=1, i=1): #видимо не разобрался в функциях, не понимаю, почему функция выводит None
    while i < y:
        z = z * x
        i += 1


print(my_func(2, 4))

# Задание 5
def my_sum():
    result = 0
    stop = False
    while not stop:
        number = input('Введите числа через пробел или Q/q для выхода - ').split()

        res = 0
        for i in range(len(number)):
            if number[i] == 'q' or number[i] == 'Q':
                stop = True
                break
            else:
                res = res + int(number[i])
        result = result + res
        print(f'Текущая сумма {result }')
    print(f'Ваш финальный результат {result}')


my_sum()

# Задание 6
def int_func(*args):
    ask_some_words = input("Введите слово: ")
    print(ask_some_words.title())
    return


int_func()
