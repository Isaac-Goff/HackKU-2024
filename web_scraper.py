from bs4 import BeautifulSoup
import requests
from SentimentAnalysis import CompareWebsites

class WebScraper:

    def __init__(self, userURL):
        self.keywordGetter = CompareWebsites()
        self.userURL = userURL
        self.trustedURL = 'https://www.bbc.com/search?q='
        self.userPage = requests.get(self.userURL)
        self.trustedPage = requests.get(self.trustedURL)

    def searchTrustedPage(self):
        

        self.keywordGetter.find_keywords()
        pass

    def scrapeTrustedPage(self):
        pass

    def scrapeUserPage(self):
        pass