import csv
import os


class Item:
    pay_rate = 0.85
    """Список для вывода экземпляров """
    all = []

    def __init__(self, name: str, price: int, amount: int):
        """инициализация имени, цены, количества"""
        self.__name = name
        self.price = price
        self.amount = amount
        self.all.append(self)
        super().__init__()
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

        if not os.path.isfile("items.csv"):
            raise FileNotFoundError("Отсутствует файл item.csv")

        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            list_reader = list(reader)

            if len(list_reader) == 5:
                for line in reader:
                    items = Item(line['name'], line['price'], line['quantity'])

            elif len(list_reader) < 5 or len(list_reader) > 5:
                raise InstantiateCSVError("Файл item.csv поврежден")


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


class Phone(Item):

    def __init__(self, name: str, price: int, amount: int, number_of_sim: int):
        """ Инициализатор атрибутов класса Phone по средству наследования от Item"""
        super().__init__(name, price, amount)
        self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self) -> int:
        """ Геттер для колчиества сим-карт """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int):
        """ Сеттер для выеявлении ошибки при недопустимом значении кол-ва сим-карт"""
        if number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = number_of_sim

    def __add__(self, other):
        """ Маг метод для сложение экземпляров разных классов """
        if isinstance(other, Item):
            return self.amount + other.amount


class MixinLog:

    def __init__(self):
        """ атрибут язык"""
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self) -> str:
        """Изменяет язык"""
        if self.language == "EN":
            self.__language = 'RU'
        elif self.language == "RU":
            self.__language = 'EN'
        return self.__language


class KeyBoard(Item, MixinLog):

    def __init__(self, name: str, price: int, amount: int):
        """ Наследование атрибутов от классов"""
        super().__init__(name, price, amount)
        MixinLog.__init__(self)


class InstantiateCSVError(Exception):
    """модуль для вывода ошибок"""
    __module__ = Exception.__module__

    def __init__(self, massage):
        self.massage = massage

    def __str__(self):
        return self.massage
