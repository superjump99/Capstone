import pandas as pd
import os
from matplotlib import pyplot as plt
import seaborn as sns


df = pd.read_csv("D:\카카오톡 받은 파일\me.csv")
print(df.keys())                    # Order Date', 'Sales', 'Quantity', 'Discount', 'Profit', 'Year', 'Month'
dfOD = df.groupby('Order Date')

dateOrder = dfOD.agg({'Quantity' : 'sum',
                     'Sales' : 'mean',
                      'Discount' : 'mean',
                      'Profit' : 'mean'})

dateOrder = dateOrder.reset_index()

print(dateOrder)
if not os.path.exists("MergeDate.csv"):
    dateOrder.to_csv("MergeDate.csv",index=False)

