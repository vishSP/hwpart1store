class Item:
    """размер скидки"""
    pay_rate = 0.85
    """Список для вывода экземпляров """
    all = []

    def __init__(self, name, price, amount):
        """инициализация имени, цены, количества"""
        self.name = name
        self.price = price
        self.amount = amount
        self.all.append(self)

        self.with_discount = 0
        self.total_price = 0

    def apply_discount(self):
        """применение скидки"""
        self.price = self.price * self.pay_rate
        return self.price

    def calculate_total_price(self):
        """подсчет полной цены товара"""
        self.total_price = self.price * self.amount
        return self.total_price
