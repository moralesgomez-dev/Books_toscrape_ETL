import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"

def scrape_books():
    current_url = BASE_URL
    books = []

    try:
        while current_url:
            response = requests.get(current_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            for book in soup.select(".product_pod"):
                title = book.h3.a["title"]
                price = book.select_one(".price_color").text.strip()
                availability = book.select_one(".availability").text.strip()
                rating = book.select_one(".star-rating")["class"][1]
                books.append((title, price, availability, rating))

            next_button = soup.select_one(".next a")
            current_url = urljoin(current_url, next_button["href"]) if next_button else None

    except requests.RequestException as e:
        print(f"Error de scraping: {e}")

    return books