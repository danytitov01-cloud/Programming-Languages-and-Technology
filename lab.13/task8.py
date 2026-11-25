# Лабораторная работа №13
# Задание 8. Система заказов
# Титов Даниэль, ИС 25-22

from collections import deque

orders = deque([
    {"number": 101, "name": "Пицца"},
    {"number": 102, "name": "Бургер"},
    {"number": 103, "name": "Суши"}
])

def add_order(number, name):
    orders.append({"number": number, "name": name})
    print("Заказ добавлен.")

def process_order():
    if orders:
        order = orders.popleft()
        print("Обработан заказ:", order)
    else:
        print("Очередь заказов пуста.")

def search_order(number):
    for order in orders:
        if order["number"] == number:
            print("Заказ найден:", order)
            return

    print("Заказ не найден.")

def show_orders():
    if orders:
        print("Оставшиеся заказы:")
        for order in orders:
            print(order)
    else:
        print("Заказов нет.")


add_order(104, "Шаурма")
search_order(102)
process_order()
show_orders()