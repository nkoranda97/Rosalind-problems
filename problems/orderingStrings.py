from itertools import product

def generate_products(text, n):
    products = [''.join(combo) for i in range(1, n+1) for combo in product(text, repeat=i)]
    return products

def custom_sort_key(product, order):
    rank = {char: index for index, char in enumerate(order)}
    return [rank[char] for char in product]

def order_products(text, n):
    products = generate_products(text, n)
    products.sort(key=lambda x: custom_sort_key(x, text))
    return products

if __name__ == '__main__':
    text, n = 'VWRMDUTJNP', 4
    ordered_products = order_products(text, n)
    with open('/Users/nick/Desktop/output.txt', 'w') as f:
        for product in ordered_products:
            f.write(product + '\n')
