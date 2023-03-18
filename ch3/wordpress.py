import requests
from bs4 import BeautifulSoup


def wordpress(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    posts = []
    for article in soup.find_all("article", "blog-post"):
        post = {
            "title": div.header.a.text.strip(),
            "date": div.header.time.span.text.strip(),
            "link": div.header.a["href"],
            "summary": div.find("div", "inner-desc").text.strip()
        }
        posts.append(post)
    return posts


if __name__ == '__main__':
    URL = "https://decing.tw"
    posts = wordpress(URL)
    print(f"{len(posts)} articles retrieved. The first 3:")
    print("--")
    for post in posts[:3]:
        print(article)
        print("--")
