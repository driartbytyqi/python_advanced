from itertools import product

import pandas as pd

product = ["Apples","Bannas","organges","grapes","pineapple"]

sales = [150,200,180,90,60]


sales_series = pd.Series(sales, index=product)

print(sales_series)

print(sales_series['grapes'])