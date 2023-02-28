import requests
from bs4 import BeautifulSoup


def get_tag_text(url, tag):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "html.parser")
            return soup.find(tag).text
    except Exception as e:
        print(f"Exception when getting URL: {url} and tag: {tag}\n{e}")
    return None


if __name__ == "__main__":
    # Normal case
    print(get_tag_text("https://compthinking-dev.github.io/py-web-scraping/ch1/connect.html", "h1"))

    # h2 does not exist
    print(get_tag_text("https://compthinking-dev.github.io/py-web-scraping/ch1/connect.html", "h2"))

    # URL does not exist
    print(get_tag_text("http://non-existing.domain/connect.html", "h1"))

    print("The end of program")
