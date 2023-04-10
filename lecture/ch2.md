# 2. 使用 Beautiful Soup 解構網頁

## 2-1. 不要重覆造輪子：寫爬蟲之前

* 寫程式之前：再想想是否有其他方法
* 先搜尋 "爬蟲", 下載", "Crawler", "Downloader" 等關鍵字, 可能已經有人做好：
  * 現成的服務 (e.g., YouTube Downloader, 券商 App, 財報狗)
  * 打包好的資料 (e.g., [維基百科](https://zh.wikipedia.org/wiki/Wikipedia:%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%8B%E8%BD%BD))
  * 現成的函式庫 (e.g., [ComicCrawler](https://github.com/eight04/ComicCrawler))
* 需要自己寫爬蟲時，考慮以下順序
  * API (YouTube, imdb, Twitter, ...)
  * URL 或網址連結是否有規則 (日期, 代號, ...)
  * 若網頁使用 AJAX (非同步更新)，可能有隱藏的 API Endpoint
    * 範例: [櫃買中心 > 上櫃個股日成交資訊](http://www.tpex.org.tw/web/stock/aftertrading/daily_trading_info/st43.php?l=zh-tw)
  * 網頁很複雜時，試試"列印此網頁"或行動版網頁
* "直接開始爬網頁"永遠是最後一個選項

## 2-2. 使用 BeautifulSoup - 定位標籤元件

* 範例程式: `ch2/find.py`
* [範例網頁](http://compthinking-dev.github.io/py-web-scraping/ch2/blog.html)
* 定位元件
    * `find()` 回傳第一個找到的元件; `find_all()` 回傳所有元件
    * `find_all(tag_name, tag_attrs, ..., **kwargs)`
    * 95% 的時間只會用到 tag name 與 tag attributes (class, id, name, 其他特殊屬性)
* 取得文字
    * `.text (get_text())` (包含該元件以下所有階層標籤內的文字)
    * `stripped_strings`: 回傳 iterator object, 需巡覽以取出其中的值
* 補充資料
    * https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all
    * https://www.crummy.com/software/BeautifulSoup/bs4/doc/#get-text
    * https://www.crummy.com/software/BeautifulSoup/bs4/doc/#strings-and-stripped-strings

## 2-3. 使用 BeautifulSoup - 巡覽網頁結構

* 範例程式: `ch2/navigation.py`
* [範例網頁](http://compthinking-dev.github.io/py-web-scraping/ch2/table.html)
* 雖然 `find()`, `find_all()` 可以處理大部分問題, 但有時候巡覽網頁結構 (parent, children, next and previous siblings) 比較好用
* 影片中提到了 iterator object, 想深入了解 iterator 是什麼的話可參考: [Python 中的 Iterator 是什麼](https://compthinking.dev/posts/what-is-iterator-in-python)

```
body
  - div
    - h2
    - p
    - table
      - thead
        - tr
          - th
          - th
          - th
          - th
      - tbody
        - tr
          - td
          - td
          - td
          - td
            - a
              - img
        - tr
        - ...        
```

* 補充資料 
    * https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree

# 2-4. 正規表示式 (Regular Expression)

* 範例程式: `ch2/regex.py`
* 簡潔表示字串結構的方式
* [RegEx Pal](http://www.regexpal.com/): 線上測試 regex

```
計算思維是應用計算機科學的概念與方法，如問題拆分、抽象表示與邏輯推理，來更好地解決日常生活的問題。在人工智慧及資料科學已是顯學的今日，有越來越多人，尤其是跨領域的知識工作者（如商管、財金、新聞、社會科學等），對於「寫程式、計算思維或工具如何幫助或加值自己的專業」非常有興趣，而 Python 是我們認為最適合新手入門的程式語言。為什麼？不只是因為 Python 語言本身的簡潔與優雅，更因為它廣泛的用途，從最基本的自動化生活瑣事，到網站開發、機器學習、科學計算、桌面應用、資料分析與視覺化等，幾乎所有你想讓電腦為你代勞的事情都能夠用 Python 實作。因此，計算思維學院創辦初期便聚焦在 Python 相關的知識與應用場景。

聯絡我們 support@compthinking.dev
https://compthinking.dev
```

* 常見的 rules
  * Email: `[A-Za-z0-9\._+]+@[A-Za-z0-9\._]+\.(com|org|edu|net|dev)`
  * URL: `http(s)?://[A-Za-z0-9\.]+`
    * 所有中文字(不含標點符號): `[\u4e00-\u9fa5]+`
    * (查詢標點符號的 Unicode: [Unicode 查詢](http://unicodelookup.com))
    * Google it! e.g., "email regex", "phone regex", "中文字 regex", ...
* 補充資料
  * https://docs.python.org/3/library/re.html
  * https://atedev.wordpress.com/2007/11/23/%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%A4%BA%E5%BC%8F-regular-expression/
