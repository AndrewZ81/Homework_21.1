from classes.exceptions import NotEnoughSpaceError, NotEnoughProductQuantityError, UnknownProductError
from classes.storage import Storage
from costants import STORE_DEFAULT_CAPACITY


class Store(Storage):  # Создаём класс-наследник Склад и переопределяем методы

    def __init__(self, items: dict[str, int], capacity: int = STORE_DEFAULT_CAPACITY):
        """
        Создает защищенные атрибуты Товары на складе и Вместимость склада
        :param items: Товары на складе (словарь вида {наименование товара: количество товара}
        :param capacity: Вместимость склада (целое число)
        """
        self._items = items
        self._capacity = capacity

    def add(self, name: str, quantity: int = 0) -> str:
        """
        Добавляет товар на склад или увеличивает кол-во товара
        :param name: Наименование товара
        :param quantity: Количество товара
        :return: Форматированную строку с результатом операции
        """
        free_space = self.get_free_space
        if quantity > free_space:  # Если свободного места меньше, чем нужно
            raise NotEnoughSpaceError
        try:  # Если свободного места достаточно
            self._items[name.lower()] += quantity
            return f"На склад добавлен товар {name.lower()} в кол-ве {quantity}"
        except KeyError:
            self._items[name.lower()] = quantity
            return f"На склад добавлен НОВЫЙ товар {name.lower()} в кол-ве {quantity}"

    def remove(self, name: str, quantity: int = 0) -> str:
        """
        Уменьшает кол-во товара на складе или удаляет товар со склада
        :param name: Наименование товара
        :param quantity: Количество товара
        :return: Форматированную строку с результатом операции
        """
        try:
            if quantity > self._items[name.lower()]:
                raise NotEnoughProductQuantityError
            self._items[name.lower()] -= quantity
            if self._items[name.lower()] == 0:
                self._items.pop(name.lower())
                return f"После удаления со склада товара {name.lower()} " \
                       f"в кол-ве {quantity} он закончился"
            return f"Со склада удалён товар {name.lower()} в кол-ве {self._items[name.lower()]}"
        except KeyError:
            raise UnknownProductError

    @property
    def get_items(self) -> dict:
        """
        Возвращает содержимое склада
        :return: Словарь формата {наименование товара: количество товара}
        """
        return self._items

    @property
    def get_free_space(self) -> int:
        """
        Возвращает свободное место на складе
        :return: Целое число
        """
        quantity: int = sum(self._items.values())
        return self._capacity - quantity

    @property
    def get_unique_items_count(self) -> int:
        """
        Возвращает количество уникального товара на складе
        :return: Целое число
        """
        return len(self._items)
