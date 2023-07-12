from inventory_report.product import Product
from typing import Optional


class Inventory:
    _data: list[Product]

    def __init__(self, data: Optional[list[Product]] = None) -> None:
        if data is None:
            self._data = []
        else:
            self._data = data

    @property
    def data(self) -> list[Product]:
        return self._data

    def add_data(self, data: list[Product]) -> None:
        self._data.extend(data)
