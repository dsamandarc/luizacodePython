celular = '456'
carts = [['123', '1', '800.00', 1], ['456', '1', 40.00, 2]]

product = list(filter(lambda item:item[0]== celular, carts))
print(product[0][2])