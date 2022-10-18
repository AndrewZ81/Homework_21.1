from classes.store import Store
from classes.shop import Shop

my_store = Store(
    {
        "печенье": 100,
        "яйца": 50,
        "хлеб": 20,
        "молоко": 10,
        "книги": 5
    },
    300
)

my_shop = Shop(
    {
        "печенье": 10,
        "яйца": 5,
        "хлеб": 1,
        "молоко": 1
    },
    30
)

storages: dict[str, object] = {  # Создаём словарь из всех хранилищ для обработки запроса
    "склад": my_store,
    "магазин": my_shop
}