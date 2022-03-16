import pandas as pd
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="motizuki",
  password="",
  database="planetone"
)

cursor = db.cursor()

# cursor.execute("CREATE TABLE sales (date VARCHAR(255), value VARCHAR(255), product VARCHAR(255), qtd VARCHAR(255))")

## Initial test
# sale = {
#     'date': ['13/02/2022', '16/02/2022'],
#     'value': [500, 300],
#     'product': ['beans', 'rice'],
#     'qtd': [50, 70] 
# }

# sales_df = pd.DataFrame(sale)

# print(sales_df)

## Second test
sales_df = pd.read_csv("sales.csv")

print(sales_df)

# cheatshet
# sales_df.loc[:,:] # means every line and every column
# axis=0 is line and axis=1 is column

## Methods 
# print(sales_df.head()) # shows the first 5 lines, you can do (10) the number you want
# print(sales_df.shape) # shows the number of lines and columns
# print(sales_df[['date', 'product']]) # to get a column, a column is a pd.Series object
# print(sales_df.loc[0:1]) # returns the line from it's id 
# print(sales_df.loc[sales_df['product'] == "rice", ['qtd']]) # returns all lines that product is rice
# sales_df.merge(another_df) # merges tables with in commom columns

## Creating new column
# sales_df['comission'] = sales_df['value'] * 0.05 # creates a column from an existing one
# sales_df['tax'] = 0 # creates a whole new column
# print(sales_df)

## Adding new lines
# sales = {
#     'date': ['13/02/2022', '16/02/2022'],
#     'value': [500, 300],
#     'product': ['beans', 'rice'],
#     'qtd': [50, 70] 
# }
# sales_df2 = pd.DataFrame(sales)
# sales_df = pd.concat([sales_df, sales_df2], ignore_index = 'true')
# print(sales_df)

## dropping lines and columns
# print(sales_df.drop(0, axis=0)) # drops line
# print(sales_df.drop('value',axis=1)) # drops column

# for row in sales_df.itertuples():
#     cursor.execute('''
#         INSERT INTO sales (date, value, product, qtd)
#         VALUES(?,?,?,?)
#         ''',
#         row.date,
#         row.value,
#         row.product,
#         row.qtd
#     )

add_record = """INSERT INTO sales(date, value, product, qtd) VALUES (%s, %s, %s, %s)"""

for row in sales_df.itertuples():
    cursor.execute(add_record, (str(row.date), str(row.value), str(row.product), str(row.qtd)))

db.commit()