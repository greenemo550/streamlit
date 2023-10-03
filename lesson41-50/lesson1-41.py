import pandas as pd

movie_data = {
    'Movie Title': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Genre': ['Action', 'Comedy', 'Drama', 'Action', 'Drama', 'Comedy', 'Romance', 'Action', 'Comedy', 'Romance'],
    'Release Year': [2018, 2019, 2020, 2019, 2020, 2018, 2019, 2018, 2020, 2021],
    'Rating': [4.5, 4.2, 4.7, 4.3, 4.0, 3.8, 4.1, 4.6, 3.9, 4.4],
    'Box Office (in $M)': [100, 55, 75, 120, 85, 50, 60, 110, 40, 65]
}

df = pd.DataFrame(movie_data)

average_rating = df[df["Release Year"] == 2020]["Rating"].mean()
print(average_rating)

box_office_100m = df[df["Box Office (in $M)"] >= 100]
print(box_office_100m["Movie Title"])

genre_gruop = df.groupby("Genre").size()
print(genre_gruop)

rating_gruop = df[(df["Release Year"] == 2018) | (df["Release Year"] == 2019)]
high_score = rating_gruop[rating_gruop["Rating"] == rating_gruop["Rating"].max()]
print(high_score["Movie Title"].values[0])

low_revenue = df[df["Box Office (in $M)"] == df["Box Office (in $M)"].min()]
print(low_revenue["Genre"].values[0], low_revenue["Rating"].values[0])