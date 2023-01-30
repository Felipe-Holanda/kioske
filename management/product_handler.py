from menu import products


def menu_report():
    product_count = len(products)
    average_price = sum([product['price']
                        for product in products]) / product_count
    average_price = round(average_price, 2)
    average_type = {}
    for product in products:
        if product['type'] in average_type:
            average_type[product['type']] += 1
        else:
            average_type[product['type']] = 1
    most_common = max(average_type, key=lambda x: average_type[x])
    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common}"


def get_product_by_id(id: int) -> (dict[str] | None):
    try:
        if type(id) != int:
            raise TypeError("product id must be an int")
        for product in products:
            if product['_id'] == id:
                return product
            elif product == products[-1]:
                return {}
    except TypeError as e:
        raise e


def get_products_by_type(param: str) -> (list[dict[str]] | None):
    try:
        if type(param) != str:
            raise TypeError("product type must be a str")
        return [product for product in products if product['type'] == param]
    except TypeError as e:
        raise e


def add_product(menu: list, **kwargs) -> (dict[str | int]):
    try:
        if not type(menu) == list:
            raise TypeError("You must pass a list to MENU param.")
        if not menu:
            new_id = 1
        else:
            sorted_list = sorted(menu, key=lambda k: k['_id'])
            last_id = sorted_list[-1]['_id']
            new_id = last_id + 1
        product = {'_id': new_id}
        for key, value in kwargs.items():
            product[key] = value
        menu.append(product)
        return product
    except TypeError as e:
        raise e
