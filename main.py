# 35
def plus_two(number):
    try:
        result = 2 + number
        print(result)
    except TypeError:
        print("Ожидаемый тип данных — число!")

try:
    user_input = float(input("Введите число: "))
    plus_two(user_input)
except ValueError:
    print("Ошибка ввода. Введите корректное число.")

# 36
def access_element(arr, index):
    try:
        value = arr[index]
        print(f"Элемент с индексом {index}: {value}")
    except IndexError:
        print(f"Ошибка: Индекс {index} выходит за границы массива")
my_array = [1, 2, 3, 4, 5]
access_element(my_array, 2)
access_element(my_array, 10)
