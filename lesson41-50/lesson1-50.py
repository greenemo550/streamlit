import pandas as pd

data = {
    'Artist': ['The Beatles', 'The Rolling Stones', 'Elton John', 'Mariah Carey', 'Elvis Presley'],
    'Albums Sold (millions)': [600, 240, 300, 200, 210],
    'Grammy Awards': [7, 2, 5, 5, 3],
    'Active Years': ['1960-1970', '1962-present', '1969-present', '1990-present', '1954-1977']
}

df = pd.DataFrame(data)

top_sales = df[df["Albums Sold (millions)"] == df["Albums Sold (millions)"].max()]
print(top_sales[["Artist", "Albums Sold (millions)"]])

current_year = pd.Timestamp.now().year

df["Start Year"] = df["Active Years"].str.split("-").str[0].astype(int)
df["End Year"] = df["Active Years"].str.split("-").str[1].replace("present", str(current_year)).astype(int)

df["Duration"] = df["End Year"] - df["Start Year"]

longest_active = df[df["Duration"] == df["Duration"].max()]
print(longest_active["Artist"])

average = df["Albums Sold (millions)"].mean()
print(average)

