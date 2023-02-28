import requests
import json
import math


API_KEY = "YOUR_API_KEY"
OMDB_URL = f"http://www.omdbapi.com/?apikey={API_KEY}"


def get_data(url):
    data = requests.get(url).json()
    return data if data["Response"] == "True" else None


def get_movie_ids_by_keyword(keywords):
    movie_ids = list()
    query = "+".join(keywords.split())  # e.g., "Iron Man" -> Iron+Man
    url = f"{OMDB_URL}&s={query}"
    data = get_data(url)
    """ e.g.,
    {
      "Search": [
        {
          "Title": "Iron Man",
          "Year": "2008",
          "imdbID": "tt0371746",
          "Type": "movie",
          "Poster": "https://images-na.ssl-images-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_SX300.jpg"
        },
        ...
      ],
      "totalResults": "101",
      "Response": "True"
    }
    """
    if data:
        # 第一頁的電影 ids
        for item in data["Search"]:
            movie_ids.append(item["imdbID"])

        total = int(data["totalResults"])  # 搜尋結果總數
        num_pages = math.ceil(total/10)

        # 取得第二頁以後的資料
        for page in range(2, num_pages + 1):
            url = f"{OMDB_URL}&s={query}&page={page}"
            data = get_data(url)
            if data:
                for item in data["Search"]:
                    movie_ids.append(item["imdbID"])
    return movie_ids


def get_movie_by_id(movie_id):
    url = f"{OMDB_URL}&i={movie_id}"
    data = get_data(url)
    return data if data else None


if __name__ == "__main__":
    keyword = "iron man"
    movie_ids = get_movie_ids_by_keyword(keyword)
    print(f"Key word: {keyword} returned {len(movie_ids)} movies")
    movies = list()
    for m_id in movie_ids:
        print(f"Retrieving {m_id}...")
        movie_data = get_movie_by_id(m_id)
        movies.append(movie_data)    
    print("First 3 movies:")
    for m in movies[:3]:
        print(f"{m['Title']} ({m['Year']}) by {m['Actors']}")
    with open("imdb_data.json", "w", encoding="utf-8") as f:
        json.dump(movies, f, ensure_ascii=False, indent=2)
