from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        "2",
        "Coca-cola",
        "Ambev",
        "01/01/2021",
        "01/01/2022",
        "1",
        "keep it cold",
    )

    assert product.id == "2"
    assert product.product_name == "Coca-cola"
    assert product.company_name == "Ambev"
    assert product.manufacturing_date == "01/01/2021"
    assert product.expiration_date == "01/01/2022"
    assert product.serial_number == "1"
    assert product.storage_instructions == "keep it cold"
