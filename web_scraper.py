import bs4
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
import wget
import requests
from SentimentAnalysis import CompareWebsites

class WebScraper:

    def __init__(self, userURL):
        self.driver = webdriver.Chrome()
        self.keywordGetter = CompareWebsites()
        self.userURL = userURL
        self.trustedURL = 'https://www.bbc.com/search?q='
        self.userPage = requests.get(self.userURL)
        self.trustedPage = requests.get(self.trustedURL)

    def searchTrustedPage(self):
        keywords = self.getKeywords()

        firstKeyword = ''.join(c for c in keywords[0].replace(' ', '_') if c.isalpha())
        self.trustedURL += firstKeyword
        print(self.trustedURL)

        self.getKeywords(self.trustedURL)

    def scrapePage(self, altURL=''):
        try:
            self.driver.current_url
        except:
            self.driver = webdriver.Chrome
        if altURL == '':
            self.driver.get(self.userURL)
        else:
            self.driver.get(altURL)
        time.sleep(.75)
        self.driver.execute_script("window.scrollTo(0, 35000);")
        time.sleep(.75)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        self.driver.close()
        return soup

    def getText(self, altURL=''):
        cleaned_text = []
        soup = self.scrapePage(altURL if altURL != '' else self.userURL)

        for p in soup.findAll('p'):
            temp = p.get_text()
            cleaned_text.append(temp)
        print(cleaned_text)

        finalText = ''.join(cleaned_text)
        print(finalText)
        return finalText

    def getKeywords(self, altURL=''):
        text = self.getText(altURL if altURL != '' else self.userURL)
        keywords = self.keywordGetter.find_keywords(text)
        print(keywords)
        return keywords


webscraper = WebScraper('https://www.cnn.com/2024/04/13/americas/guatemala-genocide-trial-maya-ixil-indigenous-intl-latam/index.html')
webscraper.searchTrustedPage()

