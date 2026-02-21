import requests
import bs4

url = "https://www.goodreads.com/quotes"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(response.text, "html.parser")
quotes = soup.findAll("div", class_="quoteText")

for quote in quotes :
    print(quote.text if quote else "No quote found")

print(len(quotes))