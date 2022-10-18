from classes.courier import Courier
from classes.exceptions import BaseError
from classes.request import Request
from data import storages
from costants import STOP_LIST
from functions import show_all_stores_and_items

def get_user_interface() -> None:
    """
    Реализует пользовательский интерфейс
    :return: None
    """
    print("Доброго времени суток")
    stop_list = STOP_LIST  # Стоп-лист для выхода из программы
    while True:
        show_all_stores_and_items()
        raw_request = input("Введите запрос в формате "
                         "'Доставить 3 (кол-во) печенье (что) из склад (откуда) в магазин (куда)'\n"
                         "Для завершения работы наберите 'stop' или 'стоп'\n")
        if raw_request in stop_list:
            print("Всего хорошего")
            break
        try:
            user_request = Request(storages, raw_request)
        except BaseError as e:
            print(e.error_message)
            continue

        user_courier = Courier(storages, user_request)  # Доставляем товар

        try:
            user_courier.move_items()
        except BaseError as e:
            print(e.error_message)
            continue


if __name__ == "__main__":

    get_user_interface()
