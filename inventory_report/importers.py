from typing import Dict, Type
from inventory_report.product import Product
from abc import ABC, abstractmethod
import csv
import json


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        raise NotImplementedError(
            """Classes derivadas de Importer precisam implementar o método
            import_data"""
        )


class JsonImporter(Importer):
    def __init__(self, path: str) -> None:
        super().__init__(path)

    def import_data(self) -> list[Product]:
        list_products = []

        file = open(self.path)
        data = json.load(file)

        for product in data:
            list_products.append(
                Product(
                    id=product["id"],
                    product_name=product["product_name"],
                    company_name=product["company_name"],
                    manufacturing_date=product["manufacturing_date"],
                    expiration_date=product["expiration_date"],
                    serial_number=product["serial_number"],
                    storage_instructions=product["storage_instructions"],
                )
            )

        return list_products


class CsvImporter(Importer):
    def __init__(self, path: str) -> None:
        super().__init__(path)

    def import_data(self) -> list[Product]:
        list_products = []

        with open(self.path, "r") as data:
            reader = csv.reader(data)
            next(reader)

            for line in reader:
                (
                    id,
                    product_name,
                    company_name,
                    manufacturing_date,
                    expiration_date,
                    serial_number,
                    storage_instructions,
                ) = line

                list_products.append(
                    Product(
                        id,
                        product_name,
                        company_name,
                        manufacturing_date,
                        expiration_date,
                        serial_number,
                        storage_instructions,
                    )
                )

            return list_products


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
