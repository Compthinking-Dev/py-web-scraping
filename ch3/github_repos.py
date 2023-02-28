import requests
from bs4 import BeautifulSoup


def github(url):
    repos = []
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    for div in soup.find_all("div", {"itemprop": "owns"}):
        sub_divs = div.find_all("div", recursive=False)
        repo = {
            "description": list(sub_divs[0].stripped_strings),
            "metadata": list(sub_divs[1].stripped_strings)
        }
        repos.append(repo)
    return repos


if __name__ == '__main__':
    URL = "https://github.com/orgs/mozilla/repositories"
    repos = github(URL)
    print(f"{len(repos)} repos retrieved.")
    for repo in repos:
        print(f"Name: {repo['description'][0]}. Language: {repo['metadata'][0]}")
