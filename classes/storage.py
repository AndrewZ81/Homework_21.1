from abc import ABC, abstractmethod


class Storage(ABC):  # Создаём абстрактный класс Хранилище для всех типов хранилищ

    @abstractmethod
    def add(self, name: str, quantity: int = 0) -> str:
        """
        Добавляет товар в хранилище или увеличивает кол-во товара
        :param name: Название товара
        :param quantity: Количество товара
        :return: Форматированную строку с результатом операции
        """
        pass

    @abstractmethod
    def remove(self, name: str, quantity: int = 0) -> str:
        """
        Уменьшает кол-во товара в хранилище
        :param name: Название товара
        :param quantity: Количество товара
        :return: Форматированную строку с результатом операции
        """
        pass

    @abstractmethod
    def get_items(self) -> dict:
        """
        Возвращает содержимое хранилища
        :return: Словарь формата {товар: количество}
        """
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        """
        Возвращает свободное место в хранилище
        :return: Целое число
        """
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        """
        Возвращает количество уникального товара в хранилище
        :return: Целое число
        """
        pass
