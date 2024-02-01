import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/aradh/OneDrive/Desktop/flipkart/mobiles.csv")

# Convert 'Price' column to numeric (remove '₹' and convert to int)
df['Price'] = df['Price'].replace('[\₹,]', '', regex=True).astype(int)

# Plotting bar chart for Prices
plt.figure(figsize=(10, 6))
plt.bar(df['Product Name'], df['Price'])
plt.xlabel('Product Name')
plt.ylabel('Price (in INR)')
plt.title('Prices of Products')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
