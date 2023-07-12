from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self) -> None:
        super().__init__()

    def count_stock(self) -> str:
        data = self.inventory
        count: dict[str, int] = {}
        string = ""

        for product in data:
            if product.company_name not in count:
                count[product.company_name] = 1
            else:
                count[product.company_name] += 1

        for company, counter in count.items():
            name = f"- {company}: {counter}\n"
            string += name

        return string

    def generate(self) -> str:
        return (
            f"Oldest manufacturing date: { super().oldest_manufactured() }\n"
            f"Closest expiration date: {super().closest_expiration()}\n"
            f"Company with the largest inventory: {super().largest_stock()}\n"
            f"Stocked products by company:\n"
            f"{ self.count_stock()}"
        )
