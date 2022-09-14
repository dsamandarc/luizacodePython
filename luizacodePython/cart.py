cart = [] 

def add_item_cart(item, cart):
    cart.append(item)
    return cart

def get_all_item_cart():
    return cart

def execute():
    id_user = input("Insira o ID do usuário:")
    id_product = input("Insira o ID do produto")
    price_product = float(input("Insira o preço do produto:"))
    quantity_product = int(input("Insira a quantidade de produto:"))
    item = [id_product, id_user, price_product, quantity_product]
    cart = add_item_cart(item, cart)
    print(cart)
    
execute()
