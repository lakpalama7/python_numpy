import pandas as pd
import numpy as np

df = pd.DataFrame({'Product': ['Carrots', 'Broccoli', 'Banana', 'Banana',
                               'Beans', 'Orange', 'Broccoli', 'Banana'],
                   'Category': ['Vegetable', 'Vegetable', 'Fruit', 'Fruit',
                                'Vegetable', 'Fruit', 'Vegetable', 'Fruit'],
                   'Quantity': [8, 5, 3, 4, 5, 9, 11, 8],
                   'Amount': [270, 239, 617, 384, 626, 610, 62, 90]})
print(df)

# get total sales of each product

pivot = df.pivot_table(index=['Product'], values=['Amount'], aggfunc='sum')
print(pivot)

# get total sales of each category
pivot = df.pivot_table(index=['Category'], values=['Amount'],aggfunc='sum')
print(pivot)

# get total sales by Category and product both

pivot = df.pivot_table(index=['Category','Product'],values='Amount', aggfunc='sum')
print(pivot)

# get mean, median, minimum sales by category
pivot = df.pivot_table(index='Category', values=['Amount'], aggfunc={'mean','median','min'})
print(pivot)

# get mean, median, min sales by product
pivot = df.pivot_table(index=['Product'], values=['Amount'], aggfunc={'mean','median','min'})
print(pivot)