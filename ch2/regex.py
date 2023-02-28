import requests
import re
from bs4 import BeautifulSoup


if __name__ == "__main__":
    resp = requests.get("http://compthinking-dev.github.io/py-web-scraping/ch2/blog.html")
    soup = BeautifulSoup(resp.text, "html.parser")

    # 找出所有 "h" 開頭的標題文字
    titles = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    for title in titles:
        print(title.text.strip())

    # 利用 regex 找出所有 "h" 開頭的標題文字
    for title in soup.find_all(re.compile("h[1-6]")):
        print(title.text.strip())

    # 找出所有以 "Python" 開頭的標籤
    headers = soup.find_all("h6")
    for h in headers:
        if h.text.startswith("Python"):
            print(h.text)

    # 利用 regex 找出以 "Python" 開頭的標籤
    for h in soup.find_all("h6", string=re.compile("^Python")):
        print(h.text)

    # 找出所有以 "Python" 開頭且含 "Azure" 的標籤
    headers = soup.find_all("h6")
    for h in headers:
        if h.text.startswith("Python") and "Azure" in h.text:
            print(h.text)

    # 利用 regex 找出所有以 "Python" 開頭且含 "Azure" 的標籤
    for h in soup.find_all("h6", string=re.compile("^Python.*Azure.*")):
        print(h.text)
