# Лабораторная работа №13
# Задание 1. Список покупок
# Титов Даниэль, ИС 25-22

def add_product(products, name):
    products.append(name)
    print("Товар добавлен.")

def remove_product(products, name):
    if name in products:
        products.remove(name)
        print("Товар удалён.")
    else:
        print("Товар не найден.")

def show_products(products):
    if products:
        print("Список покупок:")
        for product in products:
            print("-", product)
    else:
        print("Список пуст.")


products = ["Хлеб", "Молоко"]

add_product(products, "Яблоки")
remove_product(products, "Молоко")
remove_product(products, "Сыр")

show_products(products)