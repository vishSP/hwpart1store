import pytest

from main import Item


@pytest.fixture
def item():
    """фикстура"""
    return Item(name='тест', price=20000, amount=5)


def test_not_found_file(item):
    with pytest.raises(FileNotFoundError):
        item.instantiate_from_csv()
