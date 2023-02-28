# 5. 資料儲存

## 5-1. 儲存為 JSON 與 CSV 檔

* `ch5/json_read_write.py`
* `ch5/json_to_csv.py`
* 讀寫 JSON 檔
  * 讀取: `json.load()`
  * 寫入: `json.dump()`
* `pandas.read_json()` 可以直接把格式簡單的 JSON 轉成 DataFrame
* `pandas.DataFrame()` 可以把 dictionary 轉成 DataFrame
  * 可以處理 key to list of values, 也可以處理 list of dictoinaries
  * `.to_csv()`: 將 DataFrame 轉換成 csv

## 5-2. 儲存圖片 (PTT Beauty 板圖片下載)

* `ch5/ptt_beauty.py`
  * 下載圖片: `urllib.request.urlretrieve()`

* 流程
  * 取得今日所有文章的超連結 (與單元 3-6 相同: `ch3/ptt_gossiping.py`)
  * 連結到文章內容, 在裡面尋找圖片網址 (imgur.com)
  * 使用文章標題作為資料夾名稱，下載圖片

* 用正規表示式擷取合法網址。以下都是一張圖片的合法網址
```
http://i.imgur.com/A2wmlqW.jpg,
http://i.imgur.com/A2wmlqW  # 沒有 .jpg
https://i.imgur.com/A2wmlqW.jpg
http://imgur.com/A2wmlqW.jpg
https://imgur.com/A2wmlqW.jpg
https://imgur.com/A2wmlqW
http://m.imgur.com/A2wmlqW.jpg
https://m.imgur.com/A2wmlqW.jpg
```
* 將下載圖片時使用的網址統一為 i.imgur.com 開頭, .jpg 結尾
  
## 5-3. 儲存資料到資料庫 SQLite

* `ch5/sqlite_operation.py`
* 關聯式資料庫 (Relational Database): 如同一張張的表格, 每張表格有不同欄位
* 使用資料庫的好處: 加快查詢速度 (建立索引), 進階查詢功能, 多執行緒或平行讀寫等
* SQLite: 小而全, 小而美, 支援 SQL 標準語法, 零安裝, Python 直接內建支援, 處理 TB 規模的資料, 支援每日百萬次瀏覽的網站沒有問題
* GUI: http://sqlitebrowser.org/
* 語法查詢 (建議直接 Google 搜尋最快): http://www.1keydata.com/tw/sql/sqlselect.html