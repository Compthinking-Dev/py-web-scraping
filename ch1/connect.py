import requests
from bs4 import BeautifulSoup

resp = requests.get("https://compthinking-dev.github.io/py-web-scraping/ch1/connect.html")
soup = BeautifulSoup(resp.text, "html.parser")
print(soup.find("h1").text)
