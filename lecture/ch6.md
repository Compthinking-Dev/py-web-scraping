# 6. 動態網站爬蟲

## 6-1. 台銀法拍屋 - 使用 Selenium

* `ch6/bot_house.py`
* Selenium Webdriver - 與其模仿瀏覽器，不如直接使用瀏覽器
  * 優點: 能夠解決大部分的障礙；不需要慢慢分析送出請求所需的參數
  * 缺點: 執行速度, 例外處理, e.g., 不定時彈出廣告, 網頁結構變動
  * 只要電腦上有安裝該瀏覽器, 就不用再額外下載 Webdriver 執行檔
* Webdriver 可以做的事:
  * 定位網頁元件 (find_element by id/tag/class/link_text/xpath...)
  * 點擊, 輸入文字, 選擇選單, 拖拉...
  * 下載目前看到的網頁原始碼 (後續使用 Beautifulsoup 解析並取得資訊)
* 範例: http://www.bot.com.tw/house/default.aspx 
  * (第一次啟動 Webdriver 時, Windows 可能會跳出防火牆警告, 請准許)
* Webdriver 啟動時的選項
```
options.add_argument('--headless')  # headless mode. 可加速執行速度
options.add_argument("--deny-permission-prompts")  # 拒絕瀏覽器跳出 pop-up, e.g., 問你要不要分享目前位置
```
  
## 6-2. PCHome 搜尋 - 使用 Selenium 及 requests.get()

* `ch6/pchome.py`
* 範例: https://24h.pchome.com.tw/
  * 從首頁輸入搜尋字串，點擊搜尋，點選品牌條件，分析結果
* 透過開發者工具觀察網頁更新時的 XHR requests，可以直接得到搜尋 API 的 Endpoint
  * `https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=[SEARCH_TERM]`

## 6-3. 臺灣證交所每日收盤行情 - 使用 Selenium 及 requests.post()
* `ch6/twse_etf_trading.py`
* `ch6/twse_etf_trading_post.py`
* 範例: https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html
  * 透過下拉式選單選擇年月日及 ETF 分類，再選擇顯示全部資料
* 透過開發者工具觀察網頁更新時的 XHR requests，可以直接得到資料 API 的 Endpoint
  *  POST form data to `https://www.twse.com.tw/zh/exchangeReport/MI_INDEX`