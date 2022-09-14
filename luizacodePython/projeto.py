cart = []

#for i in range(3):

id_user = input("Insira o ID do usuário:")
id_product = input("Insira o ID do produto")
price_product = float(input("Insira o preço do produto:"))
quantity_product = int(input("Insira a quantidade de produto"))

item = [id_user, id_product, price_product, quantity_product]

def add_item_cart():
    cart.append(item)
    return cart

# def get_all_items_cart(): 
#     #return todos os itens do carrinho 
#     pass

# def get_item_cart_by_id(id_product):
#     #return 

# def remove_item_id(id_product):
#     #remove o item do carrinho que tem esse produto
#     pass


def get_all_items_cart():
    print('Carrinho :', cart)
    return cart

def get_item_cart_by_id(id_product):
    for items_cart in cart:
        if items_cart[1] == id_product:
            print('Item:', items_cart[1])
            return items_cart[1]

def remove_item_id(id_product):
    print("Antes da Remoção:", cart)
    for items_cart in cart:
        if items_cart[1] == id_product:
            cart.remove(items_cart)

print("Após remoção:", cart)
return cart