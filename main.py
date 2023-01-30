from menu import products
from management.product_handler import get_product_by_id, get_products_by_type, add_product, menu_report
from management.tab_handler import calculate_tab

if __name__ == "__main__":
    # Seus prints de teste aqui
    print(get_product_by_id(28))

    print(get_products_by_type('drink'))

    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }

    print(add_product(products, **new_product))

    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]

    print(calculate_tab(table_1))
    print(calculate_tab(table_2))

    print(menu_report())


# Primeiro Output deve ser:

# {"_id": 28, "description": "Ricotta with berry and mint", "price": 27.81, "rating": 5, "title": "Ricotta", "type": "dairy"}

# Segundo Output deve ser:
"""
[
  {
    '_id': 32,
    'description': 'Mix of rum, lemon juice, mint, sugar and sparking water',
    'price': 27.61,
    'rating': 4,
    'title': 'Mojito',
    'type': 'drink'
},
  {
    '_id': 37,
    'description': 'Homemade cola drink with lemon juice and 2 ice cubes',
    'price': 28.96,
    'rating': 5,
    'title': 'Fresh Nuka-Cola',
    'type': 'drink'
  }
]
"""

# Terceiro Output deve ser:

"""
{
  'title': 'X-Python',
  'price': 5.0,
  'rating': 5,
  'description': 'Sanduiche de Python',
  'type': 'fast-food',
  '_id': 1
}
"""

# Quarto Output deve ser:

"""
{'subtotal': '$216.1'}
{'subtotal': '$188.29'}
"""

"""
Products Count: <contagem_de_produtos>
Average Price: $<preco_medio>
Most Common Type: <tipo_mais_comum>
"""
