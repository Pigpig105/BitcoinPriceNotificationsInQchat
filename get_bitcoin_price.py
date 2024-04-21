import requests
from bs4 import BeautifulSoup

# Pull HTML bitcoin data
page_to_scrape = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# Find all span elements containing the price
untrimmedPrices = soup.findAll("span", attrs={"class": "sc-f70bb44c-0 jxpCgO base-text"})

if untrimmedPrices:
    # Check if any matching elements were found
    if len(untrimmedPrices) > 0:
        # Extract the text content of the first matching element
        price_element = untrimmedPrices[0]
        price = price_element.text.strip()
    else:
        print("Price element not found on the page")
else:
    print("No matching elements found on the page")