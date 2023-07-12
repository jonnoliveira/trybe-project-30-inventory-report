from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        "2",
        "Coca-cola",
        "Ambev",
        "01/01/2021",
        "01/01/2022",
        "1",
        "keep it cold",
    )

    assert str(product.__str__()) == (
        "The product 2 - Coca-cola "
        "with serial number 1 "
        "manufactured on 01/01/2021 "
        "by the company Ambev "
        "valid until 01/01/2022 "
        "must be stored according to the following instructions: "
        "keep it cold."
    )
