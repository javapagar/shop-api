from src.products.application.product_saver import ProductSaver


def test_product_saver(repo_product, product_name, product_quantity, product_price):
    saver = ProductSaver(repo_product)

    uuid_product_saved = saver.save(
        name=product_name, quantity=product_quantity, price=product_price
    )

    product = repo_product.find(uuid_product_saved)
    assert uuid_product_saved == product.uuid
