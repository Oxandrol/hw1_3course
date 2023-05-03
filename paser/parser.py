from pprint import pprint
import requests
from bs4 import BeautifulSoup

URL = "https://kinogo.biz/new/"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}


def get_html(url):
    response = requests.get(url, headers=HEADERS)
    return response


def get_data(html, size=None):
    soup = BeautifulSoup(html, 'html.parser')
    size = int(size) if size else None
    items = soup.find_all("div", class_="shortstory")
    movies = []
    for item in items:
        card = {
            "title": item.find("div", class_="zagolovki").find("a").get("title"),
            "url": item.find("div", class_="zagolovki").find("a").get("href"),
            "rating": item.find("div", class_="ratinggreen").find("span", class_="rat").getText(),
            "description": item.find("div", class_="desk").getText().strip(),
            "image": item.find("img").get("src")
        }
        movies.append(card)
        if size and len(movies) == size:
            break
    return movies


def parser(size=None):
    html = get_html(URL)
    if html.status_code == 200:
        movies = get_data(html.text, size)
        return movies
    raise Exception("Error in parser!")
