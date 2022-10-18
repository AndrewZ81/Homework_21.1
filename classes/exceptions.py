class BaseError(Exception):
    error_message = "Что-то пошло не так :-("


class NotEnoughSpaceError(BaseError):
    error_message = "Недостаточно свободного места.\n"


class NotEnoughProductQuantityError(BaseError):
    error_message = "Недостаточно товара.\n"


class TooManyDifferentProductsError(BaseError):
    error_message = "Превышен ассортимент магазина.\n"


class BadRequestError(BaseError):
    error_message = "Вы составили запрос не по шаблону, измените его.\n"


class UnknownStorageError(BaseError):
    error_message = "Вы ввели несуществующее место отправки и/или получения.\n"


class UnknownProductError(BaseError):
    error_message = "Вы ввели несуществующий товар.\n"


