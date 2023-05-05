import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        if self.price >= 0 or self.quantity:
            return self.quantity * self.price
        else:
            "Цена или количество товара в магазине не могут быть отрицательными числами"

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        if self.price >= 0 or self.pay_rate:
            self.price = self.price * self.pay_rate
        else:
            "Цена или размер скидки не могут быть отрицательными числами"

    def __repr__(self):
        """
        Возвращает строку, содержащую печатаемое официальное представление объекта
        """
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает строку, содержащую печатаемое неформальное представление объекта
        """
        return f"{self.__name}"

    @property
    def name(self):
        """
        Геттер
        """
        return self.__name

    @name.setter
    def name(self, size):
        """
        Сеттер с проверкой, что в наименовании товара не более 10 символов
        """
        if len(size) <= 10:
            print("Наименование товара не превышает 10 символов")
            self.__name = size
        else:
            print("Наименование товара не превышает 10 символов")

    @staticmethod
    def string_to_number(str_number):
        """
        статический метод, возвращающий число из числа-строки
        """
        return int(float(str_number))

    @classmethod
    def instantiate_from_csv(cls):
        """
        класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        cls.all.clear()
        with open('../src/items.csv', 'r', encoding="cp1251", newline='', ) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

