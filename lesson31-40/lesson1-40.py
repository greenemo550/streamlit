import pandas as pd

car_data = {
    'Brand': ['Toyota', 'Honda', 'Toyota', 'Nissan', 'Honda', 'Toyota', 'Nissan', 'Honda', 'Toyota', 'Nissan'],
    'Model': ['Corolla', 'Civic', 'Camry', 'Altima', 'Accord', 'Rav4', 'Maxima', 'CR-V', 'Highlander', 'Rogue'],
    'Year': [2020, 2020, 2021, 2021, 2021, 2020, 2019, 2019, 2021, 2020],
    'Sales': [1000, 1100, 980, 1025, 875, 1300, 950, 1125, 1050, 925],
    'Price': [20000, 21000, 23000, 24000, 22000, 25000, 27000, 26000, 29000, 21000]
}

df = pd.DataFrame(car_data)
top_sales_year = df[df["Year"] == 2021]
top_sales = top_sales_year[top_sales_year["Sales"] == top_sales_year["Sales"].max()]
print(top_sales["Brand"].values[0], top_sales["Model"].values[0])

average_toyota = df[df["Brand"] == "Toyota"]["Price"].mean()
print(average_toyota)

df["Revenue"] = df["Sales"] * df["Price"]
brand_group = df.groupby("Brand")["Revenue"].mean()
print(brand_group)

high_sales = df[df["Price"] >= 25000]["Sales"].sum()
print(high_sales)

average_year = df.groupby("Year")["Revenue"].sum()
print(average_year)
