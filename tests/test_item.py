"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def fixture_object():
    return Item("something", 1000.0, 3)


@pytest.fixture
def fixture_object_negative():
    return Item("something", - 1000.0, - 3)


def test_item(fixture_object):
    assert fixture_object.name == "something"
    assert fixture_object.price == 1000.0
    assert fixture_object.quantity == 3


def test_calculate_total_price(fixture_object):
    assert fixture_object.price * fixture_object.quantity == 3000.0


def test_apply_discount(fixture_object):
    fixture_object.pay_rate = 0.15
    fixture_object.apply_discount()
    assert fixture_object.price == 150.0


def test__repr__(fixture_object):
    assert repr(fixture_object) == "Item('something', 1000.0, 3)"


def test__str__(fixture_object):
    assert str(fixture_object) == 'something, 1000.0, 3'


def test_check_attribute(fixture_object):
    assert type(fixture_object.name) == str
    assert type(fixture_object.price) == float
    assert type(fixture_object.quantity) == int


def test_apply_discount_negative(fixture_object_negative):
    fixture_object_negative.pay_rate = - 0.15
    fixture_object_negative.apply_discount()
    assert "Цена или размер скидки не могут быть отрицательными числами" == "Цена или размер скидки не могут быть " \
                                                                            "отрицательными числами"


def test_calculate_total_price_negative(fixture_object_negative):
    assert "Цена или количество товара в магазине не могут быть отрицательными числами" == "Цена или количество " \
                                                                                           "товара в магазине не " \
                                                                                           "могут быть отрицательными " \
                                                                                           "числами"


def test_string_to_number(fixture_object):
    assert fixture_object.string_to_number("7") == 7
    assert fixture_object.string_to_number("7.0") == 7
    assert fixture_object.string_to_number("7.7") == 7


def test_setter_name(fixture_object):
    assert len(fixture_object.name) <= 10
    assert len(fixture_object.name + "wwwwwwww") > 10

