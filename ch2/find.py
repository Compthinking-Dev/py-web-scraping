import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    resp = requests.get("http://compthinking-dev.github.io/py-web-scraping/ch2/blog.html")
    soup = BeautifulSoup(resp.text, "html.parser")

    # 取得第一篇 blog (h4)
    print(soup.find("h4"))  # 也可以寫成 soup.h4

    # 取得第一篇 blog 主標題
    print(soup.h4.a.text)

    # 使用 key=value 取得標籤元件
    print(soup.find(id="post-p"))

    # 當 key 含特殊字元時, 使用 dict 取得元件
    # print(soup.find(post-topic="current-ai"))  # 會導致 SyntaxError
    print(soup.find(None, {"post-topic": "current-ai"}))

    # 取得所有 blog 主標題, 使用 tag
    main_titles = soup.find_all("h4")
    for title in main_titles:
        print(title.a.text)

    # 取得所有 blog 主標題, 使用 class
    # 以下寫法皆相同:
    main_titles = soup.find_all("h4", "card-title")
    # main_titles = soup.find_all("h4", {"class": "card-title"})
    # main_titles = soup.find_all("h4", class_="card-title")
    for title in main_titles:
        print(title.a.text)

    # 取得各篇 blog 的所有文字
    divs = soup.find_all("div", "content")
    for div in divs:
        # 方法一, 使用 text (會包含許多換行符號)
        # print(div.text)
        # 方法二, 使用 tag 定位
        # print(div.h6.text.strip(), div.h4.a.text.strip(), div.p.text.strip())
        # 方法三, 使用 .stripped_strings
        print(list(s for s in div.stripped_strings))
