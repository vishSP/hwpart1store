from main import Item
import pytest

"""фикстура"""


@pytest.fixture
def item():
    return Item(name='тест', price=20000, amount=5)


def test_repr(item):
    """Проверяет маг метод repr """
    assert item.__repr__() == "Item('тест',  20000,  5)"


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
    assert item.is_integer(5) == True
    assert item.is_integer(5.0) == True
    assert item.is_integer(5.5) == False
