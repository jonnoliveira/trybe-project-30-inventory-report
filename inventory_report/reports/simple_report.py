from inventory_report.inventory import Inventory
from datetime import date, datetime
from operator import attrgetter


class SimpleReport:
    def add_inventory(self, inventory: Inventory) -> None:
        self.inventory = inventory.data

    def oldest_manufactured(self) -> str:
        """
        https://siddharth1.medium.com/1-understanding-operator-itemgetter-attribute-or-operator-itemgetter-attribute-27e61754d1fa
        https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-itemgetter/
        """
        oldest_item = min(self.inventory, key=attrgetter("manufacturing_date"))
        oldest = oldest_item.manufacturing_date

        return oldest

    def closest_expiration(self) -> str:
        today = str(date.today())

        return min(
            product.expiration_date
            for product in self.inventory
            if str(datetime.strptime(product.expiration_date, "%Y-%m-%d"))
            > today
        )

    def largest_stock(self) -> str:
        largest: dict[str, int] = {}

        for product in self.inventory:
            if product.company_name not in largest:
                largest[product.company_name] = 1
            else:
                largest[product.company_name] += 1

        return max(larg for larg in largest)

    def generate(self) -> str:
        return (
            f"Oldest manufacturing date: { self.oldest_manufactured() } "
            f"Closest expiration date: { self.closest_expiration() } "
            f"Company with the largest inventory: { self.largest_stock() } "
        )
