# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет
# свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент
# товаров. Ваша задача — создать класс `Store`, который можно будет использовать для создания различных магазинов.
# 1. Создай класс `Store`:
# 2. Создай несколько объектов класса `Store`:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них
# несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену,
# убери товар и запрашивай цену.


class Store:
    def __init__(self, name, address, initial_items=None):
        self.name = name
        self.address = address
        self.items = initial_items if initial_items is not None else {}

    def add_item(self, item_name, price):
        """Добавление товара в ассортимент."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаление товара из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """Получение цены товара по его названию. Если товар отсутствует, возвращается None."""
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        """Обновление цены товара."""
        if item_name in self.items:
            self.items[item_name] = new_price

# Создание трех объектов класса Store с начальными товарами
store1 = Store("Fresh Market", "Тухачевского 46", {"apples": 0.5, "bananas": 0.75})
store2 = Store("Магнит", "Доваторцев 55", {"oranges": 0.6, "grapes": 1.2})
store3 = Store("Чижик", "Шпаковская 78", {"bread": 1.0, "milk": 0.9})

# Добавление товара
store1.add_item("pears", 0.8)
print(store1.items)  # {'apples': 0.5, 'bananas': 0.75, 'pears': 0.8}

# Обновление цены
store1.update_price("bananas", 0.85)
print(store1.items)  # {'apples': 0.5, 'bananas': 0.85, 'pears': 0.8}

# Удаление товара
store1.remove_item("apples")
print(store1.items)  # {'bananas': 0.85, 'pears': 0.8}

# Запрос цены
price_of_pears = store1.get_price("pears")
print(f"Цена груш: {price_of_pears}")  # Цена груш: 0.8

price_of_apples = store1.get_price("apples")
print(f"Цена яблок: {price_of_apples}")  # Цена яблок: None (так как товар удалён)