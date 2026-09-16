class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity):
        self.products.append((product, quantity))

    def total_cost(self):
        total = 0

        for product, quantity in self.products:
            total += product.price * quantity

        return total

    def show_order(self):
        print("Заказ:")

        for product, quantity in self.products:
            cost = product.price * quantity
            print(f"{product.name}: {quantity} шт. = {cost}")

        print(f"Итоговая стоимость: {self.total_cost()}")


product1 = Product("Ноутбук", 300000)
product2 = Product("Мышь", 5000)
product3 = Product("Клавиатура", 15000)

order = Order()

order.add_product(product1, 1)
order.add_product(product2, 2)
order.add_product(product3, 1)

order.show_order()
