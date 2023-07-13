from inventory_report.importers import CsvImporter, JsonImporter
from inventory_report.inventory import Inventory
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from typing import List


def process_report_request(file_paths: List[str], report_type: str) -> str:
    if not is_report_type_valid(report_type):
        raise ValueError("Report type is invalid.")

    inventory = Inventory()
    for path in file_paths:
        report_process(path, inventory)

    if report_type == "simple":
        result = SimpleReport()
    else:
        result = CompleteReport()

    result.add_inventory(inventory)
    return result.generate()


def is_report_type_valid(report_type: str) -> bool:
    return report_type == "simple" or report_type == "complete"


def report_process(path: str, inventory: Inventory) -> None:
    if path.endswith(".csv"):
        data_csv = CsvImporter(path)
        inventory.add_data(data_csv.import_data())

    elif path.endswith(".json"):
        data_json = JsonImporter(path)
        inventory.add_data(data_json.import_data())
