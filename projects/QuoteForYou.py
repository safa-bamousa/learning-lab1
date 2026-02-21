import requests
import bs4
import random

headers = {
    "User-Agent": "Mozilla/5.0"
}
url_love = "https://www.goodreads.com/quotes/search?utf8=%E2%9C%93&q=love&commit=Search"
url_science = "https://www.goodreads.com/quotes/search?utf8=%E2%9C%93&q=science&commit=Search"
url_life = "https://www.goodreads.com/quotes/search?utf8=%E2%9C%93&q=life&commit=Search"

quote_abt = input("What type of quote you want? (science, life , or love): ").lower()

def search_by_url(url):
    response = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quoteText")
    random_quote = random.choice(quotes)
    print(random_quote.text if random_quote else "No quote found")

urls = {
    "love" : url_love,
    "life" : url_life,
    "science" : url_science
}

if quote_abt in urls :
    search_by_url(urls[quote_abt])
else:
    print("Invalid choice!")