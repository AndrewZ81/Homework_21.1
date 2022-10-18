from data import storages


def show_all_stores_and_items():  # Получаем ассортимент всех хранилищ в форматированном виде
    print("Ассортимент товаров такой.\n")
    for i, k in storages.items():
        print(f"{i.capitalize()} хранит:\n")
        for m, n in k.get_items.items():
            print(f"{m.capitalize()} - {n}")
        print()
