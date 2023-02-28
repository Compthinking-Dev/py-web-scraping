import requests
from bs4 import BeautifulSoup


def wordpress(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    articles = []
    for div in soup.find_all("article", "blog-post"):
        article = {
            "title": div.header.h1.a.text.strip(),
            "date": div.header.find("div", "post-meta").time.span.text.strip(),
            "link": div.h1.a["href"],
            "summary": div.find("div", "inner-desc").text.strip()
        }
        articles.append(article)
    return articles


if __name__ == '__main__':
    URL = "https://decing.tw"
    articles = wordpress(URL)
    print(f"{len(articles)} articles retrieved. The first 3:")
    print("--")
    for article in articles[:3]:
        print(article)
        print("--")
