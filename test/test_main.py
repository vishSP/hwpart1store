from main import Item
from main import Phone
import pytest


@pytest.fixture
def item():
    """фикстура"""
    return Item(name='тест', price=20000, amount=5)


@pytest.fixture
def phone():
    return Phone(name='iPhone 14', price=20000, amount=5, number_of_sim=3)


def test_repr(item):
    """Проверяет маг метод repr """
    assert item.__repr__() == "Item('тест', '20000', 5)"


def test_str(item):
    """Проверяет метод str """
    assert item.__str__() == "тест"


def test_apply_discount(item):
    """проверяет скидку"""
    item.pay_rate = 0.8
    assert item.apply_discount() == 16000.0
    assert item.price == 16000.0


def test_calculate_total_price(item):
    """Проверяет полную цену (товар*колво товара)"""
    assert item.calculate_total_price() == 100000


def test_name(item):
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    with pytest.raises(Exception):
        item.name('Длина наименования товара превышает 10 символов.')


def test_instantiate_from_csv(item):
    assert len(item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'тест'


def test_is_integer(item):
    assert item.is_integer(5) is True
    assert item.is_integer(5.0) is True
    assert item.is_integer(5.5) is False


def test_get_attributes(phone):
    """Проверка получения атрибутов экземпляра класса Phone"""
    assert phone.name == 'iPhone 14'
    assert phone.price == 20000
    assert phone.amount == 5
    assert phone.pay_rate == 0.85
    assert phone.number_of_sim == 3
    assert phone.pay_rate == 0.85


def test_change_number_of_sim_correct_data(phone):
    """Проверка изменения атрибута number_of_sim"""
    phone.number_of_sim = 1

    assert phone.number_of_sim == 1


def test_change_number_of_sim_incorrect_data(phone):
    """
    Проверка вызова исключения при попытке изменить количество сим-карт
    на число не равное 1 или 2
    """
    with pytest.raises(ValueError):
        phone.number_of_sim = 3


def test_add(item, phone):
    """
    Проверка сложения экземпляра класса Item с экземпляром класса Phone
    """
    assert phone + item == 10
    assert phone + phone == 10


def test_object_name_repr(phone):
    """Проверка отображения информации об объекте класса Phone для разработчиков"""
    assert repr(phone) == "Phone('iPhone 14', '20000', 5)"
