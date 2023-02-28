import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://www.kingstone.com.tw/basic/2013120484184/"

    print("未附加 User-Agent header, 回傳錯誤訊息")
    resp = requests.get("https://www.kingstone.com.tw/basic/2013120484184/")
    print(resp.text)

    print("附加 User-Agent header 後, 回傳正確資料") 
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/109.0.0.0 Safari/537.36"}
    resp = requests.get("https://www.kingstone.com.tw/basic/2013120484184/", headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")
    print(list(soup.find("div", "division_main col2 clearfix").stripped_strings))