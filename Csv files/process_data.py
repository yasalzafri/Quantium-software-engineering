import pandas as pd
import csv

# loading csv file // reading

df1 = pd.read_csv(
    r'C:/Users/USER\Desktop/Quantium Task 1/Csv files\daily_sales_data_0.csv')

print(df1)
df2 = pd.read_csv(
    r'C:/Users/USER/Desktop/Quantium Task 1/Csv files/daily_sales_data_1.csv')

print(df2)

df3 = pd.read_csv(
    r'C:/Users/USER\Desktop/Quantium Task 1/Csv files/daily_sales_data_2.csv')

print(df3)

# Combine all into one data frame ,ignore_index=True ka use tab hota hai jab hum multiple DataFrames ko combine (concat) karte hain.
# 🔹 Without ignore_index=True
# Har DataFrame apna original index le kar aata hai.
# Dekho indexes 0,1,0,1 repeat ho rahe hain (kyunki df1 aur df2 dono ke apne indexes the).

df = pd.concat([df1, df2, df3], ignore_index=True)

# filter only pink morsels

df = df[df['product'] == 'pink morsel']

# Create sales column

df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

df['sales'] = (df['price'] * df['quantity'])

# Keep only required columns

final_output = df[['product', 'sales', 'date', 'region']]

# save to csv

final_output.to_csv(
    r'C:/Users/USER/Desktop/Quantium Task 1/Csv files/final_output.csv', index=False)
