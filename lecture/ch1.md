# 1. 環境設定與網頁爬蟲初探

## 1-1. 環境設定: 安裝 Python 及使用 venv

* `https://www.python.org/downloads/`
* Add python, pip to PATH
```
# 確認 Python 及 pip 可以使用
C:\Users\chill>python --version
Python 3.10.2

C:\Users\chill>pip --version
pip 21.2.4 from C:\Users\chill\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)
```
```
# 創建虛擬環境 (目錄名稱: `web-scraping`)
python -m venv web-scraping
# 進入虛擬環境
web-scraping/Scripts/activate
# 離開虛擬環境
deactivate
```

## 1-2. 使用 Visual Studio Code

* https://code.visualstudio.com/
* Extensions
  * Python
* 指定 Interpreter 到虛擬環境
* 執行程式及設定中斷點


## 1-3. 網頁文件解構與網頁爬蟲初探

* 網頁 = 由標籤 (tag) 所組成的階層式文件
* HTML (網頁的骨架結構)、CSS (網頁的樣式) 與 JavaScript (在瀏覽器端執行，負責與使用者互動的程式功能)。
* [範例網頁](http://compthinking-dev.github.io/py-web-scraping/ch1/connect.html)
* 範例程式
  * `ch1/connect.py`
  * `ch1/try_connect.py`
```
html
  -head
    -meta (<meta charset="utf-8">)
    -title (<title>Python 網頁爬蟲入門實戰 | 計算思維學院 Compthinking.Dev</title>)
    -link (<link href="...bootstrap.min.css">)
    -script (<script> ... </script>)
  -body
    -div
      -h1 (<h1>歡迎來到 Python 網頁爬蟲入門實戰！</h1>)
      -p (<p class="">計算思維是應用計算機科學的概念與方法...</p>)
      -p
        -a (<a href="https://compthinking.dev/">了解更多 </a>)
    -footer
      -div
        -p (<p class="text-muted">計算思維學院 (c) 2023</p>)
    (-script)
```
* `requests` 連線, `Beautifulsoup` parse, `find()` 找標籤, `.text` 取文字
* 網路世界是雜亂的，永遠要記得處理例外，避免爬蟲中斷
  * 網站連不上
  * 找不到網頁
  * 找不到 Tag 或 Tag 的屬性
