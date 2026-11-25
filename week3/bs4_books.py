from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
soup = BeautifulSoup(requests.get(url, timeout=10).text, "lxml")
for c in soup.select("article.product_pod"):
    a = c.select_one("h3 a")
    print(a["title"], c.select_one("p.price_color").text, urljoin(url, a["href"]))
