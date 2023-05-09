"""Здесь надо написать тесты с использованием pytest для модуля phone."""
import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def fixture_object():
    return Item("something", 1000.0, 3)


@pytest.fixture
def fixture_object_subclass():
    return Phone("phone", 100.0, 10, 20)


def test_phone(fixture_object_subclass):
    assert fixture_object_subclass.name == "phone"
    assert fixture_object_subclass.price == 100.0
    assert fixture_object_subclass.quantity == 10
    assert fixture_object_subclass.number_of_sim == 20


def test__repr__(fixture_object_subclass):
    assert repr(fixture_object_subclass) == "Phone('phone', 100.0, 10, 20)"


def test__str__(fixture_object_subclass):
    assert str(fixture_object_subclass) == 'phone'


def test_check_attribute(fixture_object_subclass):
    assert type(fixture_object_subclass.name) == str
    assert type(fixture_object_subclass.price) == float
    assert type(fixture_object_subclass.quantity) == int
    assert type(fixture_object_subclass.number_of_sim) == int


def test_number_of_sim():
    with pytest.raises(ValueError):
        Phone("phone33", 10.0, 20, -2)

def test_setter_name(fixture_object_subclass):
    assert len(fixture_object_subclass.name) <= 10
    assert len(fixture_object_subclass.name + "wwwwwwwwWWWWWW") > 10


def test_phone_isinstance(fixture_object_subclass):
    # используется для проверки принадлежности объекта к определенному классу
    assert isinstance(fixture_object_subclass, Phone)


def test_phone_issubclass(fixture_object_subclass):
    # используется для проверки, наследуется ли какой-либо класс от другого
    assert issubclass(type(fixture_object_subclass), Item)


def test__add__(fixture_object, fixture_object_subclass):
    string = "строка"
    assert fixture_object_subclass + fixture_object == 13
    assert fixture_object_subclass + fixture_object_subclass == 20
    with pytest.raises(TypeError):
         fixture_object_subclass + fixture_object + string
