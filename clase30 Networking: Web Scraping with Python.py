#web scraping is when a program or script pretends to be a browser and retrieves
#web pages, looks at those web pages, extracts information, and then looks at more web pages
#search engines scrape web pages- we call this "spidering the web" or "web crawling"

#uses of scrape
#pull data-particularly social data- who links to who?
#get your own data back out of some system that has no "export capability"
#monitor a site for new information
#spider the web to make a database for search engine

#beatiful soup  
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
