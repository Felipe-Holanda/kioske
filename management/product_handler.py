from menu import products


def get_product_by_id(id: int) -> (dict[str] | None):
    try:
        if not type(id) == int:
            raise TypeError("You must pass an integer to ID param.")
        for product in products:
            if product['_id'] == id:
                return product
    except TypeError as e:
        raise e


def get_products_by_type(param: str) -> (list[dict[str]] | None):
    try:
        if not type(param) == str:
            raise TypeError("You must pass a string to TYPE param.")
        return [product for product in products if product['type'] == param]
    except TypeError as e:
        raise e


def add_product(menu: list, **kwargs) -> (dict[str | int]):
    sorted_list = sorted(menu, key=lambda k: k['_id'])
    last_id = sorted_list[-1]['_id']
    new_id = last_id + 1
    product = {'_id': new_id}
    for key, value in kwargs.items():
        product[key] = value
    menu.append(product)
    return product


def menu_report():
    product_count = len(products)
    average_price = sum([product['price']
                        for product in products]) / product_count
    average_type = {}
    for product in products:
        if product['type'] in average_type:
            average_type[product['type']] += 1
        else:
            average_type[product['type']] = 1
    return f"Products count: {product_count} - Average price: {average_price} - Average type: {average_type}"
