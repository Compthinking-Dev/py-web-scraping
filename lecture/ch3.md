# 3. 網頁爬蟲範例實戰

## 3-1. 自由時報今日熱門新聞

* `ch3/ltn_news.py`
* 網頁: https://news.ltn.com.tw/list/breakingnews/popular
* 資料位置: `<ul class="list">` > `<li>`

## 3-2. 東森新聞今日熱門新聞

* `ch3/ebs_news.py`
* 網頁: https://news.ebc.net.tw/hot
* 資料位置: `div class="style1 white-box">`
* 送出需求時須包含 User-Agent header
```
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/109.0.0.0 Safari/537.36"}
resp = requests.get(url, headers=headers)
```

## 3-3. WordPress 部落格文章

* `ch3/wordpress.py`
* 網頁: https://decing.tw
* 資料位置: `<article class="blog-post">`


## 3-4. momo 購物網搜尋結果

* `ch3/momo_search.py`
* 網頁: https://m.momoshop.com.tw/search.momo?searchKeyword=pixel%207%20pro
* 資料位置: `<li class="goodsItemLi">`
* 送出需求時須包含 User-Agent header

## 3-5. Yahoo 奇摩電影本週新片

* `ch3/yahoo_movie.py`
* 網頁: https://tw.movies.yahoo.com/movie_thisweek.html
* 資料位置
  * 電影資訊: `<div class="release_info_text">`
  * 電影名稱及 Id: `<div class="release_movie_name">`
  * 上映日期: `<div class="release_movie_time">`
  * 海報網址: `find_previous_sibling('div', 'release_foto')`
  * 預告片網址: `find_next_sibling('div', 'release_btn color_btnbox')`
* 儲存資料為 JSON

## 3-6. PTT 八卦板今日熱門文章

* `ch3/ptt_gossiping.py`
* 網頁: https://www.ptt.cc/bbs/Gossiping/index.html
* 資料位置
  * 文章: `<div class="r-ent">`
  * 標題: `<a>` > text
  * 網址: `<a href=>`
  * 推文數: `<div class="nrec">`
  * 日期: `<div class="date">`
  * 上一頁按鈕所在: `<div class="btn-group btn-group-paging">`
* 流程
  1. 從最新頁面進入
  2. 取得此頁所有今日文章與上一頁的超連結
  3. 若此頁包含今日文章, 則連到上一頁, 回到步驟 2
  4. 若此頁沒有今日文章，則處理所有文章並結束程式
* 儲存資料為 JSON

## 3-7. GitHub Repositories 列表

* `ch3/github_repos.py`
* 網頁: https://github.com/orgs/mozilla/repositories
* 資料位置: `<div itemprop="owns">`
* 只回傳下一層（而非所有更深層的）結構: `find_all("div", recursive=False)`