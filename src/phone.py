from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        if number_of_sim > 0:
            self.number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        Phone.all.append(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Phone(\'{self.name}\', {self.price}, {self.quantity}, {self.number_of_sim})'

    def __add__(self, other):
        """
         Возвращает результат сложения экземпляров класса Phone и Item
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity
