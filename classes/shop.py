from classes.exceptions import TooManyDifferentProductsError, NotEnoughSpaceError, NotEnoughProductQuantityError, \
    UnknownProductError
from classes.storage import Storage
from costants import SHOP_DEFAULT_CAPACITY, SHOP_MAX_ITEMS


class Shop(Storage):  # Создаём класс-наследник Магазин и переопределяем методы

    def __init__(self, items: dict[str, int], capacity: int = SHOP_DEFAULT_CAPACITY):
        """
        Создает защищенные атрибуты Товары в магазине и Вместимость магазина
        :param items: Товары в магазине (словарь вида {наименование товара: количество товара}
        :param capacity: Вместимость магазина (целое число)
        """
        self._items = items
        self._capacity = capacity

    def add(self, name: str, quantity: int = 0) -> str:
        """
        Добавляет товар в магазин или увеличивает кол-во товара
        :param name: Наименование товара
        :param quantity: Количество товара
        :return: Форматированную строку с результатом операции
        """
        if self.get_unique_items_count >= SHOP_MAX_ITEMS:
            raise TooManyDifferentProductsError
        free_space = self.get_free_space
        if quantity > free_space:  # Если свободного места меньше, чем нужно
            raise NotEnoughSpaceError
        try:  # Если свободного места достаточно
            self._items[name.lower()] += quantity
            return f"В магазин добавлен товар {name.lower()} в кол-ве {quantity}"
        except KeyError:
            self._items[name.lower()] = quantity
            return f"В магазин добавлен НОВЫЙ товар {name.lower()} в кол-ве {quantity}"

    def remove(self, name: str, quantity: int = 0) -> str:
        """
        Уменьшает кол-во товара в магазине или удаляет товар из магазина
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
                return f"После удаления из магазина товара {name.lower()} в кол-ве {quantity} он закончился"
            return f"Из магазина удалён товар {name.lower()} в кол-ве {self._items[name.lower()]}"
        except KeyError:
            raise UnknownProductError

    @property
    def get_items(self) -> dict:
        """
        Возвращает содержимое магазина
        :return: Словарь формата {наименование товара: количество товара}
        """
        return self._items

    @property
    def get_free_space(self) -> int:
        """
        Возвращает свободное место в магазине
        :return: Целое число
        """
        quantity: int = sum(self._items.values())
        return self._capacity - quantity

    @property
    def get_unique_items_count(self) -> int:
        """
        Возвращает количество уникального товара в магазине
        :return: Целое число
        """
        return len(self._items)
