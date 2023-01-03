import pandas as pd

"""

ADMIN ACCESS
1. retrieve rows using rows index - input: row index, output: complete row
2. add new product in dataframe using inputs provided - input: product id, name, category, purchase quantity, available quantity, unit price, total price purchase date; output: write it in database
3. remove product given product name
4. update existing product data using provided inputs
5. consume product - input: product name, quantity consumed; output, update existing inventory of that product

STOREMAN ACCESS
4. update existing product data using provided inputs
5. consume product - input: product name, quantity consumed; output, update existing inventory of that product

"""

df = pd.read_csv("medicine_inventory.csv")
# print(df)
rows = len(df.index)


class Medicine_inventory():

    def __init__(self):
        pass

    def retrieve_rows(self, dataframe, row_id):
        if row_id < len(dataframe.index):
            return dataframe.iloc[row_id]
        else:
            return 'row doesnot exist'

    def add_new_product(self, dataframe, id, product_name, category, purchase_quantity, available_quantity, price,
                        total_price,date):
        if product_name not in dataframe['product name'].values:
            new_row = {'product id': id, 'product name': product_name, 'category': category,
                       'purchase quantity': purchase_quantity, 'available quantity': available_quantity,
                       'unit price (PKR)': price,'total price': total_price, 'purchase date': date}
            dataframe=dataframe.append(new_row, ignore_index=True)
            dataframe.to_csv("medicine_inventory.csv", index=False)
            return True
        else:
            return 'product already exists'

    def remove_product(self, dataframe, product_name):
        if product_name in dataframe['product name'].values:
            dataframe=dataframe[dataframe['product name'] != product_name]
            dataframe.to_csv("medicine_inventory.csv", index=False)
            return True
        else:
            return 'product not available'

    def update_product(self, dataframe, product_name, update_param, update_quantity):
        update_param="available quantity"
        if product_name in dataframe['product name'].values:
            val = dataframe.loc[(dataframe[dataframe['product name'] == product_name].index[0]), update_param]
            dataframe.loc[(dataframe[dataframe['product name'] == product_name].index[0]), update_param] = val + int(update_quantity)

            dataframe.to_csv("medicine_inventory.csv", index=False)
            return True
        else:
            return 'product not available'

    def consume_product(self, dataframe, product_name,  update_quantity):
        update_param="available quantity"
        if product_name in dataframe['product name'].values:
            val=dataframe.loc[(dataframe[dataframe['product name'] == product_name].index[0]), update_param]
            dataframe.loc[(dataframe[dataframe['product name'] == product_name].index[0]), update_param] =val- int(update_quantity)
            dataframe.to_csv("medicine_inventory.csv", index=False)
            return True
        else:
            return 'product not available'

'''
demo_class = Medicine_inventory()
print(demo_class.retrieve_rows(df, 1))
df = demo_class.add_new_product(df, 130, 'flgyl', 'capsule', 14, 12, 15, '01/12/2023')
print(demo_class.remove_product(df, 'asprin'))

# print(df[df['product name'] == 'brofin']['available quantity'])
# print(df)

df.to_csv("medicine_inventory.csv", index=False)
'''