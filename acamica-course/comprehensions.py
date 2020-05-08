from shopping_cost import read_shopping_data_dict
FILENAME = "ecommerce_transactions.csv"
KEY_NAME = 'item_name'
KEY_PRICE = 'item_price'

shopping_data = read_shopping_data_dict(FILENAME)

products = set([item[KEY_NAME] for item in shopping_data])
more_than_10 = [item for item in shopping_data if item[KEY_PRICE] > 10]

for product in sorted(products):
    print(product)

for item in more_than_10:
    print("{}: {}".format(item[KEY_NAME], item[KEY_PRICE]))
