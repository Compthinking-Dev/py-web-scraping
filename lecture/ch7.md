# 7. 爬蟲程式經驗談

## 被封鎖的常見原因: Timing, Policy Violation (robots.txt)

* Timing is Everything
  * 很多時候只要放慢爬蟲的動作就能解決問題, e.g., `time.sleep(1)`
* 做一隻有禮貌的爬蟲: robots.txt ([維基百科說明](https://zh.wikipedia.org/wiki/Robots.txt))
  * 目標網站希望爬蟲遵守的禮儀規範 (禁止的 User-Agent, 禁止的目錄, 禁止的檔案類型, 送請求的時間間隔...)
  * 範例
    * https://amazon.com/robots.txt
    * https://www.facebook.com/robots.txt
    * https://wordpress.com/robots.txt
    * https://tw.yahoo.com/robots.txt
  * 有時候該網站會有說明, e.g., https://www.facebook.com/apps/site_scraping_tos_terms.php

## 常用 Header 欄位、網站隱藏欄位

* 最常見的是 `User-Agent`. 其他 headers 如 `Referer` 也有看過
  * `ch7/kingstone.py`
* 網站的安全機制 (防止跨站請求偽造 CSRF) ([維基百科說明](https://zh.wikipedia.org/wiki/%E8%B7%A8%E7%AB%99%E8%AF%B7%E6%B1%82%E4%BC%AA%E9%80%A0))
  * hidden 欄位的值要先連線取得, 再一併送出 (e.g., ASP.NET 網頁的 `__VIEWSTATE` 等欄位)
  * `ch7/airtw_epa.py`

## 使用代理伺服器

* `ch7/proxy.py`
* 代理伺服器查詢: https://free-proxy-list.net/

