def avg(data):
    products = data.get('products', None)
    if products is None:
        raise ValueError('missing "products"')
    if not isinstance(products, list):
        raise ValueError('products is not list')
    if  len(products) == 0:
        raise ValueError('products list is empty')

    total_price = 0
    for product in products:
        name = product.get('name', None)
        price = product.get('price', None)
        if name is None:
            raise ValueError('missing "name"')
        if price is None:
            raise ValueError('missing "price"')
        if not isinstance(price, int) and not isinstance(price, float):
            raise ValueError('price is not number')
        total_price += price
    return round(total_price / len(products), 3)

if __name__ == '__main__':
    products = {
        'products': [{
            'name': 'Product 1',
            'price': 100
            },
        {
            'name': 'Product 2',
            'price': 700
        }, {
            'name': 'Product 3',
            'price': 300 
        }] 
    }
    print( avg(products) )