from src.item import Item


class Mixin:
    """
    Отдельный класс-миксин
    """

    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, new_language):
        if new_language in ["RU", "EN"]:
            self.__language = new_language
        else:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class KeyBoard(Item, Mixin):
    """
    Класс для товара “клавиатура”
    """
    def __init__(self, name: str, price: float, quantity: int, language="EN") -> None:
        super().__init__(name, price, quantity)
        self.language = language
