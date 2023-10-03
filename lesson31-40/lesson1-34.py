import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Igor', 'Jack'],
    'City': ['Tokyo', 'New York', 'London', 'Shanghai', 'Sydney', 'Tokyo', 'London', 'New York', 'Shanghai', 'Sydney'],
    'Temperature': [25, 20, 18, 22, 24, 23, 19, 21, 23, 22]
}

df = pd.DataFrame(data)

# 1. Tokyoに住む人々の平均気温
average_tokyo_temp = df[df["City"] == "Tokyo"]["Temperature"].mean()
print(average_tokyo_temp)

# 2. 各都市の平均気温
city_group = df.groupby("City")
average_city_temp = city_group["Temperature"].mean()
print(average_city_temp)

# 3. 最も平均気温が高い都市とその気温を特定
max_temperature_row = df[df["Temperature"] == df["Temperature"].max()]
print(max_temperature_row["City"].values[0], max_temperature_row["Temperature"].values[0])
