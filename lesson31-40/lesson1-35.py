import pandas as pd

sales_data = {
    'Product': ['Laptop', 'Desktop', 'Laptop', 'Laptop', 'Desktop', 'Desktop', 'Laptop', 'Desktop'],
    'Year': [2019, 2019, 2020, 2020, 2021, 2021, 2021, 2022],
    'Sales': [500, 300, 550, 520, 310, 350, 570, 320]
}

df = pd.DataFrame(sales_data)

# 1. 2020年のLaptopの平均売上
average = df[(df["Year"] == 2020) & (df["Product"] == "Laptop")]["Sales"].mean()
print(average)

# 2. 各製品について、売上の年ごとの合計
data_group = df.groupby(["Product", "Year"])
sum_data = data_group["Sales"].sum()
print(sum_data)

# 3. 2021年の売上が最も高い製品とその売上
top_sales = df[df["Year"] == 2021]
top_product = top_sales[top_sales["Sales"] == top_sales["Sales"].max()]
print(top_product["Product"].values[0], top_product["Sales"].values[0])
