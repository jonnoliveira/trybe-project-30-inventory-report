from typing import Dict, Type
from inventory_report.product import Product
from abc import ABC, abstractmethod


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        raise NotImplementedError(
            "Classes derivadas de Importer precisam implementar o método import_data"
        )


class JsonImporter(Importer):
    pass


class CsvImporter(Importer):
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
