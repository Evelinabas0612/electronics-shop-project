import pytest
from src.keyboard import KeyBoard


@pytest.fixture
def fixture_keyboard():
    return KeyBoard("keyboard", 1000.0, 20)


@pytest.fixture
def fixture_keyboard_negative():
    return KeyBoard("keyboard", 1000.0, 20)


def test_language(fixture_keyboard):
    assert fixture_keyboard.language == "EN"


def test_change_lang(fixture_keyboard):
    fixture_keyboard.change_lang()
    assert fixture_keyboard.language == "RU"
    fixture_keyboard.change_lang()
    assert fixture_keyboard.language == "EN"


def test_language_negative(fixture_keyboard_negative):
    with pytest.raises(AttributeError):
       fixture_keyboard_negative.language = "GR"
