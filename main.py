class Item:
    pay_rate = 0.85
    all =[]
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        self.all.append(self)

        self.with_discount = 0
        self.total_price = 0

    def apply_discount(self):
        self.price= self.price * self.pay_rate
        return self.price

    def calculate_total_price(self):
        self.total_price = self.price * self.amount
        return self.total_price


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

Item.pay_rate = 0.8  # устанавливаем новый уровень цен
item1.apply_discount()
print(item1.price)
print(item2.price)

print(Item.all)