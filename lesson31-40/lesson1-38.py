import pandas as pd

health_data = {
    'Name': ['John', 'Marry', 'Liam', 'Emma', 'Noah', 'Olivia', 'Ava', 'Sophia'],
    'Age': [28, 23, 22, 29, 30, 24, 25, 27],
    'Height (cm)': [175, 168, 170, 169, 172, 171, 167, 165],
    'Weight (kg)': [72, 55, 68, 58, 74, 57, 53, 56],
    'Activity Level': ['Low', 'Moderate', 'High', 'Low', 'Moderate', 'High', 'Low', 'Moderate']
}

df = pd.DataFrame(health_data)

average_height = df[df["Age"] >= 25]["Height (cm)"].mean()
print(average_height)

average_weight = df[df["Activity Level"] == "High"]["Weight (kg)"].mean()
print(average_weight)

correlation = df["Height (cm)"].corr(df["Weight (kg)"])
print(correlation)

high_height = df[df["Height (cm)"] == df["Height (cm)"].max()]
print(high_height["Name"].values[0], high_height["Height (cm)"].values[0])