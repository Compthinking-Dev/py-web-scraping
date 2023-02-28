import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    resp = requests.get("http://compthinking-dev.github.io/py-web-scraping/ch2/table.html")
    soup = BeautifulSoup(resp.text, "html.parser")

    # 計算課程均價
    # 取得所有課程價錢: 方法一, 使用 index
    prices = []
    rows = soup.find("table").tbody.find_all("tr")
    for row in rows:
        price = row.find_all("td")[2].text
        prices.append(int(price))
    print(sum(prices)/len(prices))

    # 取得所有課程價錢: 方法二, <a> 的 parent (<td>) 的 previous_sibling
    prices = []
    links = soup.find_all("a")
    for link in links:
        price = link.parent.previous_sibling.text
        prices.append(int(price))
    print(sum(prices) / len(prices))

    # 取得每一列所有欄位資訊: find_all("td") or row.children
    rows = soup.find("table").tbody.find_all("tr")
    for row in rows:
        # 方法一: find_all("td")
        columns = row.find_all("td")

        # 方法二: 找出 row (tr) 所有的直接 (下一層) children
        # columns = [td for td in row.children]

        # 以下執行時會報錯, 因為最後一列的 <a> 沒有 "href" 屬性
        # print(columns[0].text, columns[1].text, columns[2].text, columns[3].a["href"], columns[3].a.img["src"])

        # 取得 href 屬性前先檢查其是否存在
        if "href" in columns[3].a.attrs:
            href = columns[3].a["href"]
        else:
            href = None
        print(columns[0].text, columns[1].text, columns[2].text, href, columns[3].a.img["src"])

    # 取得每一列所有欄位文字資訊: stripped_strings
    rows = soup.find("table", "table").tbody.find_all("tr")
    for row in rows:
        print(list(s for s in row.stripped_strings))
