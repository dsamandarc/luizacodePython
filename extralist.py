# list = [100, 248.90, 88, 124.90]
# def discount(price):
# return price * (1 - 0.1)
# 1 - Given a list with n values, apply the discount function using map()
# 2 - Return values greater than 100, using ﬁlter()
# 3 - Sum all the values in the list using reduce()
# Exit:
# 1 - [90.0, 224.01000000000002, 79.2, 112.41000000000001]
# 2 - [248.9, 124.9]
# 3 - 561.8
# 1) Apply the discount function using map()
list1 = [100, 248.90, 88, 124.90]


def discount(price):
    return price*(1-0.1)

list_with_discount = list(map(discount, list1))
print(list_with_discount)
#return: [90.0, 224.01000000000002, 79.2, 112.41000000000001]

bigger_than_hund = list(filter(lambda x: x>100, list1))
print(bigger_than_hund)
#return [248.9, 124.9]

from functools import reduce
all_values = reduce(lambda x,y: x+y, list1 ,0)
print(all_values)
#return 561.8