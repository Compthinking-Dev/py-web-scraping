import requests
from bs4 import BeautifulSoup


def search_momo(url, query):
    search_url = url + "/search.momo?searchKeyword=" + query
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/109.0.0.0 Safari/537.36"}
    resp = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    items = []
    for li in soup.find_all("li", "goodsItemLi"):
        item = {
            'name': li.find("h3", "prdName").text.strip(),
            'price': li.find("b", "price").text.strip(),
            'link': url + li.a['href']
        }
        items.append(item)
    return items


if __name__ == '__main__':
    URL = "https://m.momoshop.com.tw/"
    query = 'pixel 7 pro'
    items = search_momo(URL, query)
    print(f"搜尋 {query} 共回傳 {len(items)} 筆資料")
    for i in items:
        print(i)
