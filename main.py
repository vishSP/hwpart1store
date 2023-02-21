import csv


class Item:
    """размер скидки"""
    pay_rate = 0.85
    """Список для вывода экземпляров """
    all = []

    def __init__(self, name: str, price: int, amount: int):
        """инициализация имени, цены, количества"""
        self.__name = name
        self.price = price
        self.amount = amount
        self.all.append(self)

        self.with_discount = 0
        self.total_price = 0

    def __repr__(self) -> str:
        """Привет разрабам и всем неравнадушным"""
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', {self.amount})"

    def __str__(self) -> str:
        """Чтоб могли читать обычные смертные"""
        return f'{self.name}'

    @property
    def name(self) -> str:
        """Геттер возвращающий название товара """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Сеттер, устанавливающий название товара длинной не больше 10 символов
        """
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception('Длина наименования товара превышает 10 символов.')

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """ Метод получает данные из файла и превращает в атрибуты"""
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            for line in reader:
                items = Item(line['name'], line['price'], line['quantity'])

    @staticmethod
    def is_integer(nubmer: int) -> bool:
        """проверяет является ли число целым"""
        isInt = float(nubmer).is_integer()
        return isInt

    def apply_discount(self) -> int:
        """применение скидки"""
        self.price = self.price * self.pay_rate
        return self.price

    def calculate_total_price(self) -> int:
        """подсчет полной цены товара"""
        self.total_price = self.price * self.amount
        return self.total_price
