import pandas as pd

book_data = {
    'Title': ['Book A', 'Book B', 'Book C', 'Book D', 'Book E', 'Book F', 'Book G', 'Book H'],
    'Author': ['Author 1', 'Author 2', 'Author 1', 'Author 3', 'Author 2', 'Author 4', 'Author 5', 'Author 1'],
    'Genre': ['Fiction', 'Fiction', 'Non-Fiction', 'Non-Fiction', 'Fiction', 'Fiction', 'Non-Fiction', 'Non-Fiction'],
    'Sold Copies': [5000, 7000, 4000, 3500, 5500, 6000, 3000, 4500],
    'Price': [20, 25, 15, 10, 22, 28, 12, 18]
}

df = pd.DataFrame(book_data)

average_fiction = df[df["Genre"] == "Fiction"]["Price"].mean()
print(average_fiction)

author1 = df[df["Author"] == "Author 1"]
print(author1["Title"])

top_book = df[df["Sold Copies"] == df["Sold Copies"].max()]
print(top_book[["Title", "Sold Copies"]])

genre_sales = df.groupby("Genre")["Sold Copies"].sum()
print(genre_sales)
