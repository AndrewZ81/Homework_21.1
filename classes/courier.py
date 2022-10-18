from classes.exceptions import TooManyDifferentProductsError, NotEnoughSpaceError


class Courier():
    def __init__(self, storages: dict[str, object], request: object):
        # Создаём частные атрибуты курьера для выполнения запроса
        self.__request: object = request

        self.__amount: int = self.__request.amount
        self.__product: str = self.__request.product
        self.__from_: object = storages[self.__request.from_]
        self.__to: object = storages[self.__request.to]

    def move_items(self):  # Создаем частный метод доставки товара
        self.__from_.remove(self.__product, self.__amount)
        print(f"Курьер забрал {self.__amount} {self.__product} из {self.__request.from_}")

        print(f"Курьер везет "
              f"{self.__amount} {self.__product} из {self.__request.from_} в {self.__request.to}")

        try:  # Проверяем, что доставка удачная, иначе возвращаем товар
            self.__to.add(self.__product, self.__amount)
        except TooManyDifferentProductsError as e:
            self.__from_.add(self.__product, self.__amount)
            print(f"{e.error_message}Возвращаем товар\n")
        except NotEnoughSpaceError as e:
            self.__from_.add(self.__product, self.__amount)
            print(f"{e.error_message}Возвращаем товар\n")
        else:
            print(f"Курьер доставил {self.__amount} {self.__product} в {self.__request.to}\n")
