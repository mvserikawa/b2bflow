import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

books = soup.select("article.product_pod")

book_list = []
for book in books:
    titulo = book.h3.a["title"]
    preco = book.select_one(".price_color").text
    book_list.append(f"{titulo} - {preco}")

with open("livros.txt", "w", encoding="utf-8") as f:
    for line in book_list:
        f.write(line + "\n")