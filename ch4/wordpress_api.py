import requests
import time
import json


def wordpress_api(url):
    api_url = f"{url}/wp-json/wp/v2/posts?per_page=100"
    resp = requests.get(api_url)
    total_post = int(resp.headers["x-wp-total"])
    total_pages = int(resp.headers["x-wp-totalpages"])
    articles = []
    print(f"{total_post} posts ({total_pages} pages) to retrieve")
    for page in range(1, total_pages + 1):
        print(f"Retrieving page {page}...")
        time.sleep(1)
        if page > 1:
            api_url = f"{url}/wp-json/wp/v2/posts?per_page=100&page={page}"
            resp = requests.get(api_url)
        for item in resp.json():
            article = {
                "title": item["title"]["rendered"],
                "date": item["date"],
                "link": item["link"],
                "summary": item["excerpt"]["rendered"]
            }
            articles.append(article)
    return articles


if __name__ == '__main__':
    URL = "https://decing.tw"
    articles = wordpress_api(URL)
    print(f"{len(articles)} articles retrieved. The first 3:")
    print("--")
    for article in articles[:3]:
        print(article)
        print("--")
    with open("wp_data.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
