import requests
from bs4 import BeautifulSoup


def ebc_news(url):
    hot_url = url + "/hot"
    articles = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/109.0.0.0 Safari/537.36"}
    resp = requests.get(hot_url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    for div in soup.find_all('div', 'style1 white-box'):
        article = {
            "link": f"{url}{div.a['href']}",
            "title": "",
            "summary": "",
            "datetime": ""
        }
        txt_div = div.a.find("div", "text")
        article["title"] = txt_div.find("span", "title").text.strip()
        article["summary"] = txt_div.find("span", "summary").text.strip()
        article["datetime"] = txt_div.find("span", "small-gray-text").text.strip()
        articles.append(article)
    return articles


if __name__ == '__main__':
    print('東森新聞今日熱門')
    URL = "https://news.ebc.net.tw"
    ebc_articles = ebc_news(URL)
    for article in ebc_articles:
        print(article["title"], article["datetime"])
