import requests
from bs4 import BeautifulSoup
import csv

def fetch_bbc_headlines():
        # BBCのURL
    url = 'https://www.bbc.com/news'
    
    # URLからHTMLを取得
    response = requests.get(url)
    # ステータスコードが200以外の場合にエラーを発生させる
    response.raise_for_status()

    # BeautifulSoupオブジェクトを作成
    soup = BeautifulSoup(response.text, "html.parser")

    # ニュースのタイトルを収集
    headlines = []
    for headline in soup.find_all("h3", class_="gs-c-promo-heading__title"):
        headlines.append(headline.text)

    return headlines

def save_to_csv(headlines):
     with open("bbx_headlines.csv", "w", newline="", encoding="utf-8") as file:
          writer = csv.writer(file)
          writer.writerow(["No", "Headline"])
          for i, headline in enumerate(headlines, 1):
               writer.writerow([i, headline])

if __name__ == "__main__":
        bbc_headlines = fetch_bbc_headlines()
        for i, headline in enumerate(bbc_headlines, 1):
            print(f"{i}. {headline}")
        save_to_csv(bbc_headlines)


