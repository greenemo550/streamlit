import pandas as pd

data = {
    'Country': ['Japan', 'USA', 'UK', 'Germany', 'France', 'China'],
    'Population (millions)': [126, 331, 66, 83, 67, 1441],
    'GDP (trillions)': [5.0, 21.4, 2.8, 3.9, 2.7, 14.3],
    'Continent': ['Asia', 'North America', 'Europe', 'Europe', 'Europe', 'Asia']
}

df = pd.DataFrame(data)

count_country = df.groupby("Continent").size()
print(count_country)

sorted_df = df.sort_values(by="GDP (trillions)", ascending=False)
top3_gdp = sorted_df.head(3)
print(top3_gdp[["Country", "Population (millions)", "GDP (trillions)"]])

high_pop = df[df["Population (millions)"] >= 1000]
high_gdp = high_pop[high_pop["GDP (trillions)"] >= 2.0]
print(high_gdp[["Country", "Population (millions)", "GDP (trillions)"]])

average_gdp = df.groupby("Continent")["GDP (trillions)"].mean()
print(average_gdp)