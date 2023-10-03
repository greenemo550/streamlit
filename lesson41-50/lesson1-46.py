import pandas as pd

gym_data = {
    'Member ID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    'Name': ['John', 'Marry', 'Tom', 'Anna', 'Harry', 'Eva', 'Megan', 'Ryan'],
    'Age': [25, 30, 28, 23, 35, 40, 38, 29],
    'Membership Duration (months)': [12, 24, 6, 12, 24, 6, 12, 18],
    'Monthly Fee ($)': [45, 40, 50, 45, 40, 50, 45, 42]
}

df = pd.DataFrame(gym_data)

average_price = df[df["Age"] >= 30]["Monthly Fee ($)"].mean()
print(average_price)

long_menbership = df[df["Membership Duration (months)"] >= 12]
print(long_menbership["Name"])

high_price = df[df["Monthly Fee ($)"] == df["Monthly Fee ($)"].max()]
print(high_price["Name"])

age_group = df.groupby("Age").size()
print(age_group)