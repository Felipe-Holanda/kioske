from menu import products
from management.product_handler import get_product_by_id


def calculate_tab(param: list[dict]) -> (float):
    try:
        if not type(param) == list:
            raise TypeError("You must pass a list to PARAM param.")
        total = 0.0
        for item in param:
            product = get_product_by_id(item['_id'])
            total += product['price'] * item['amount']
        return {"subtotal": f"${round(total, 2)}"}
    except TypeError as e:
        raise e
