# 4. 使用 API

## 4-1. API 簡介

### API = 網站規定好，(透過程式) 跟它要資料的方式

* Application Programming Interface
* 該網站希望你跟它要資料的方法/規則，通常比直接爬網頁方便
* 方便該網站控管資料流量/使用者驗證 (API key/token...)
* 與網站溝通的方法 (HTTP Methods):
  * GET: 直接貼上網址(及參數)就能**取得**資料 ("GET me the infomation")
  * POST: 在背景**送出**我的資料，希望 Server 能夠處理 ("SUBMIT data to the server") 
  * PUT: 在背景送出我想**更新**的資料 ("UPDATE a record in the DB")
  * DELETE: 在背景送出我想**刪除**的資料 ("REMOVE a record in the DB")
* 網站的回應格式
  * (常見) JSON, e.g., http://www.omdbapi.com/?t=iron+man&apikey=433e8713
  * (少見) XML, e.g., http://www.omdbapi.com/?t=iron+man&apikey=433e8713&r=xml
* 安裝瀏覽器插件 ("JSON/XML Formatter") 或線上轉換可方便觀察資料
    * Chrome 插件: [JSON Formatter](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa) / [XML Tree](https://chrome.google.com/webstore/detail/xml-tree/gbammbheopgpmaagmckhpjbfgdfkpadb)
    * 線上轉換: [JSON Formatter](https://jsonformatter.org)/[XML Viewer](http://codebeautify.org/xmlviewer)

## 4-2. WordPress API 取得部落格文章

* `ch4/wordpress_api.py`
* 關鍵字: wordpress api get posts
  * [Posts | REST API Handbook | WordPress Developer Resources](https://developer.wordpress.org/rest-api/reference/posts/)
  * [Pagination | REST API Handbook | WordPress Developer Resources](https://developer.wordpress.org/rest-api/using-the-rest-api/pagination/)
* API Endpoint: `https://example.com/wp-json/wp/v2/posts`
* 參數: per_page (每頁資料筆數), page (頁數)
* 範例: https://decing.tw
* 補充資料: [[Python 爬蟲] 如何爬取以 WordPress 架設的網站 Blog 文章](https://compthinking.dev/posts/wordpress-post-crawler-in-python)

## 4-3. 自由時報新聞網 API

* `ch4/ltn_news_api.py`
* 透過開發者工具，觀察網頁更新時的 XHR (XMLHttpRequest)，找尋可能的 API Endpoint
  * [XMLHttpRequest | MDN](https://developer.mozilla.org/en-US/docs/Glossary/XMLHttpRequest)
  * [XMLHttpRequest - 維基百科](https://zh.wikipedia.org/wiki/XMLHttpRequest)
* API Endpoint: `https://news.ltn.com.tw/ajax/breakingnews/popular/[page]`  
  * 須注意第一頁回傳資料格式與其他頁稍有不同

## 4-4. IMDB API

* `ch4/imdb_api.py`
* 非官方 API: https://www.omdbapi.com
  * API Endpoint: `http://www.omdbapi.com/?apikey=[yourkey]&`
  * 先輸入 email 取得 API Key
  * Search by title/ID
  * Search by keywords (使用 `page` 參數換頁)
  * 中文電影: 先確認英文名字或 imdb id
* 找出所有 "iron man" 相關影片
  * 用 keywords 搜尋所有相關影片, 記錄其 movie id
  * 用 id 搜尋所有影片, 紀錄相關資訊

## 4-5. GitHub API: Repositories 列表

* `ch4/github_api.py`
* 先到 GitHub 網站: `Settings -> Developer settings -> Personal access tokens` 取得 Token
* 直接搜尋現成套件 (github api python library)
  * [PyGithub/PyGithub: Typed interactions with the GitHub API v3](https://github.com/PyGithub/PyGithub)
  * [Introduction — PyGithub 1.58.0 documentation](https://pygithub.readthedocs.io/en/latest/introduction.html)
* 取得組織 (Organization) 資料
  * `get_organization()`, `get_repos()`
  * [Repository — PyGithub 1.58.0 documentation](https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html)
  * 範例: https://github.com/mozilla
* 取得使用者 (User) 資料
  * `get_user()`
  * [NamedUser — PyGithub 1.58.0 documentation](https://pygithub.readthedocs.io/en/latest/github_objects/NamedUser.html)
  * 範例: https://github.com/torvalds
  
## 4-6. YouTube Data API: 頻道觀看數及影片列表

* `ch4/youtube_channel_videos.py`
* 先到 [Google Developer Console](https://console.developers.google.com/) 啟用、取得自己的 API Key
* 頻道資料
  * 取得頻道 id: 在網頁原始碼中搜尋 https://www.youtube.com/channel/
  * https://developers.google.com/youtube/v3/docs/channels/list
  * 範例: https://www.youtube.com/channel/UCMUnInmOkrWN4gof9KlhNmQ
* 播放列表資料
  * https://developers.google.com/youtube/v3/docs/playlistItems/list
  * 範例: https://www.youtube.com/playlist?list=UUMUnInmOkrWN4gof9KlhNmQ
* 影片資料
  * https://developers.google.com/youtube/v3/docs/videos/list
  * 範例: https://www.youtube.com/watch?v=aeqIeeXjYQw
* 直接使用官方函式庫。善用文件中的試用區 (Try this method), 觀察 API Endpoints、所需參數、回傳資料格式、及函式呼叫方法
