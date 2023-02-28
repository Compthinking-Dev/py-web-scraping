import requests
import re
import json
from bs4 import BeautifulSoup


def get_web_page(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def get_movies(dom):
    soup = BeautifulSoup(dom, 'html.parser')
    movies = []
    divs = soup.find_all('div', 'release_info_text')
    for div in divs:
        movie = dict()
        movie['expectation'] = div.find('div', 'leveltext').span.text.strip()
        name_div = div.find('div', 'release_movie_name')
        movie['ch_name'] = name_div.a.text.strip()
        movie['eng_name'] = name_div.find('div', 'en').a.text.strip()
        movie['movie_id'] = get_movie_id(name_div.a['href'])
        foto_div = div.parent.find_previous_sibling('div', 'release_foto')
        movie['poster_url'] = foto_div.a.img['data-src']
        movie['release_date'] = get_date(div.find('div', 'release_movie_time').text)
        movie['intro'] = div.find('div', 'release_text').text.strip()
        trailer_a = div.find_next_sibling('div', 'release_btn color_btnbox').find_all('a')[1]
        movie['trailer_url'] = trailer_a['href'] if 'href' in trailer_a.attrs else ''
        movies.append(movie)
    return movies


def get_date(date_str):
    # e.g. "上映日期：2023-02-12" -> match.group(0): "2023-02-12"
    pattern = '\d+-\d+-\d+'
    match = re.search(pattern, date_str)
    if match is None:
        return date_str
    else:
        return match.group(0)


def get_movie_id(url):
    # e.g., 'https://movies.yahoo.com.tw/movieinfo_main/%E6%AD%BB%E4%BE%8D2-deadpool-2-7820.html
    try:
        movie_id = url.split('.html')[0].split('-')[-1]
    except:
        movie_id = url
    return movie_id


if __name__ == '__main__':
    URL = 'https://tw.movies.yahoo.com/movie_thisweek.html'
    page = get_web_page(URL)
    if page:
        movies = get_movies(page)
        print(f"{len(movies)} movies retrieved. Titles:")
        for movie in movies:
            print(movie["ch_name"])
        with open('yahoo_movies.json', 'w', encoding='utf-8') as f:
            json.dump(movies, f, indent=2, sort_keys=True, ensure_ascii=False)