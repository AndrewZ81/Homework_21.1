from classes.exceptions import BadRequestError, UnknownStorageError


class Request:
    def __init__(self, storages: dict[str, object], request: str):
        formatted_request: list = request.strip().lower().split(" ")  # Обрабатываем запрос

        if len(formatted_request) != 7:  # Если запрос составлен не по шаблону
            raise BadRequestError

        # Создаём атрибуты запроса
        self.amount: int = int(formatted_request[1])
        self.product: str = formatted_request[2]
        self.from_: str = formatted_request[4]
        self.to: str = formatted_request[-1]

        # Проверяем запрошенные виды хранилищ
        if self.from_ not in storages or self.to not in storages:
            raise UnknownStorageError

