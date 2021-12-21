from header import *
from pages.pages import Page

chrome.get("https://quotes.toscrape.com/search.aspx")
quote_to_scrape = Page(chrome)
quote_to_scrape.search_quote()