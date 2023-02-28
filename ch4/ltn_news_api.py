# 2
import requests
import json
import time


def ltn_news_api(url):
    articles = []
    page = 1
    while True:
        time.sleep(1)
        print(f"Retrieving page {page}...")
        api_url = f"{url}/{page}"
        resp = requests.get(api_url).json()
        if not resp["data"]:
            break
        if page == 1:  # resp["data"] is a list of dicts
            data = {}
            for i in range(len(resp["data"])):
                data[str(i)] = resp["data"][i]
        else:  # resp["data"] is a dict of dicts
            data = resp["data"]
        for v in data.values():
            article = {
                "link": v["url"],
                "title": v["title"],
                "time": v["time"]
            }
            articles.append(article)
        page += 1
    return articles


if __name__ == '__main__':
    print('自由時報今日熱門')
    URL = "https://news.ltn.com.tw/ajax/breakingnews/popular"
    ltn_articles = ltn_news_api(URL)
    print(f"{len(ltn_articles)} articles retrieved. The first 10:")
    print("--")
    for article in ltn_articles[:10]:
        print(article["title"], article["time"])
    with open("ltn_news_data.json", "w", encoding="utf-8") as f:
        json.dump(ltn_articles, f, ensure_ascii=False, indent=2)
