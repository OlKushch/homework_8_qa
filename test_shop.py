"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    cart = Cart()
    return cart


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(15) is True
        assert product.check_quantity(product.quantity) is True
        assert product.check_quantity(product.quantity + 1) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(15)
        assert product.quantity == 985

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1011)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        cart.add_product(product, 10)
        assert cart.products == {product: 10}
        cart.add_product(product, 10)
        assert cart.products == {product: 20}

    def test_remove_product(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product, 25)
        assert product not in cart.products

        cart.add_product(product, 10)
        cart.remove_product(product)
        assert product not in cart.products

        cart.add_product(product, 10)
        cart.remove_product(product, 5)
        assert cart.products == {product: 5}

    def test_clear(self, cart, product):
        cart.add_product(product, 10)
        cart.clear()
        assert cart.products == {}

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 10)
        assert cart.get_total_price() == product.price * 10

    def test_buy(self, cart, product):
        cart.add_product(product, 10)
        cart.buy()
        assert product.quantity == 990

    def test_buy_error(self, cart, product):
        cart.add_product(product, 1111)
        with pytest.raises(ValueError):
            cart.buy()
