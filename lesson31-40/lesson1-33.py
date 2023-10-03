import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Igor', 'Jack'],
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'Score': [85, 88, 82, 90, 87, 78, 93, 94, 89, 76]
}

df = pd.DataFrame(data)

filtered_df = df[df["Age"] >= 40]
average = sum(filtered_df["Score"]) / len(filtered_df["Score"])
print(average)

score_df = df[df["Score"] >= 90]
print ([i for i in score_df["Name"]])

sort_df = df.sort_values(by="Age", ascending=False)
print(sort_df)
