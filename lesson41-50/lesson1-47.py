import pandas as pd

data = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['John', 'Jane', 'Jim', 'Jack', 'Jill'],
    'Age': [28, 22, 25, 24, 23],
    'Scores': ['78,89,85', '82,91,76', '80,83,88', '78,85,90', '88,85,80']
}

df = pd.DataFrame(data)

# Scores列をカンマで分割
df[['Score1', 'Score2', 'Score3']] = df["Scores"].str.split(",", expand=True)
print(df[['Score1', 'Score2', 'Score3']])

df[['Score1', 'Score2', 'Score3']] = df[['Score1', 'Score2', 'Score3']].astype(int)

df["Average"] = df[["Score1", "Score2", "Score3"]].mean(axis=1)
print(df["Average"])
