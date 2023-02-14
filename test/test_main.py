from main import Item
import pytest

"""фикстура"""


@pytest.fixture
def item():
    return Item(name='тест', price=20000, amount=5)


"""проверяет скидку"""


def test_apply_discount(item):
    item.pay_rate = 0.8
    assert item.apply_discount() == 16000.0
    assert item.price == 16000.0


"""Проверяет полную цену (товар*колво товара)"""


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 100000
