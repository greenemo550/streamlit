import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data)
print(df)

# Ageが30以上の行を選択
filtered_df = df[df['Age'] >= 30]
print(filtered_df)

# Nameカラムだけを選択
names = df['Name']
print(names)
