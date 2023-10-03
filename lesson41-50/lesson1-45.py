import pandas as pd

product_data = {
    'Product ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Product Name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Tablet', 'Phone', 'Headphones', 'Speaker'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics'],
    'Price': [1000, 50, 80, 150, 300, 600, 70, 90],
    'Stock': [10, 100, 50, 45, 80, 30, 60, 70]
}

df = pd.DataFrame(product_data)

stock_over50 = df[df["Stock"] >= 50]["Price"].mean()
print(stock_over50)

high_price = df[df["Price"] == df["Price"].max()]
print(high_price[["Product Name", "Price"]])

low_stock = df[df["Stock"] == df["Stock"].min()]
print(low_stock[["Category", "Stock"]])

average = df.groupby("Category")["Price"].mean()
print(average)