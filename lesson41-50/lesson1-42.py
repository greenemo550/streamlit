import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah'],
    'Age': [25, None, 35, 45, 20, 30, None, 40],
    'Salary': [50000, 60000, 70000, None, None, 80000, 90000, 100000]
}

df = pd.DataFrame(data)

df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].median(), inplace=True)

print(df["Age"])
print(df["Salary"])