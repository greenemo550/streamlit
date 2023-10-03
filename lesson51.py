import requests
from bs4 import BeautifulSoup

response = requests.get("http://example.com")
response.raise_for_status()

soup = BeautifulSoup(response.content, "html.parser")

elements_with_class = soup.find_all("p", class_="important")

print(elements_with_class)



