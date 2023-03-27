import requests
from bs4 import BeautifulSoup


def ltn_news(url):
    articles = []
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    for li in soup.find("ul", "list").find_all("li"):
        a = li.find("a", "tit")
        article = {
            "link": a["href"],
            "title": a.div.h3.text.strip(),
            "time": a.find("span", "time").text.strip()
        }
        articles.append(article)
    return articles


if __name__ == "__main__":
    print("自由時報今日熱門")
    URL = "https://news.ltn.com.tw/list/breakingnews/popular"
    ltn_articles = ltn_news(URL)
    for article in ltn_articles:
        print(article["title"], article["time"])
