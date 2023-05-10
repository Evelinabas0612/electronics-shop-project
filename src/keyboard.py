from src.item import Item


class Mixin:
    """
    Отдельный класс-миксин
    """

    def __init__(self, language="EN"):
        self.language = language

    def change_lang(self):
        list_lang = ["EN", "RU"]
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"
        return self


class KeyBoard(Item, Mixin):
    """
    Класс для товара “клавиатура”
    """
    def __init__(self, name: str, price: float, quantity: int, language="EN") -> None:
        super().__init__(name, price, quantity)
        self.language = language
