import pandas as pd

real_estate_data = {
    'City': ['San Francisco', 'Los Angeles', 'Seattle', 'Portland', 'Denver', 'Austin', 'Dallas', 'Houston', 'Chicago', 'New York'],
    'State': ['CA', 'CA', 'WA', 'OR', 'CO', 'TX', 'TX', 'TX', 'IL', 'NY'],
    'Median_House_Price': [1400000, 750000, 760000, 650000, 500000, 460000, 420000, 380000, 320000, 2500000],
    'Monthly_Rent': [3400, 2500, 2300, 2100, 1900, 1600, 1500, 1400, 1800, 5000]
}
df = pd.DataFrame(real_estate_data)

max_price = df[(df["State"] == "CA")]
max_price_ca = max_price[max_price["Median_House_Price"] == max_price["Median_House_Price"].max()]
print(max_price_ca["City"].values[0], max_price_ca["Median_House_Price"].values[0])

count = len(df[df["Monthly_Rent"] >= 2000])
print(count)

state_average = df.groupby("State")["Median_House_Price"].mean()
print(state_average)

correlation_coefficient = df["Median_House_Price"].corr(df["Monthly_Rent"])
print(correlation_coefficient)

