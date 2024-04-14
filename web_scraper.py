from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
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
        self.userKeywords = ''
        self.userSentiment = ''
        self.trustedKeywords = ''
        self.trustedSentiment = ''

    def searchTrustedPage(self):
        keywords = self.getKeywords()

        firstKeyword = ''.join(c for c in keywords[0].replace(' ', '%20'))
        searchURL = self.trustedURL + firstKeyword
        print(searchURL)

        self.goToURL(searchURL)

    def goToURL(self, searchURL):
        try:
            self.driver.current_url # Force exception to reload webdriver
        except:
            self.driver = webdriver.Chrome()

        self.driver.get(searchURL)

        time.sleep(.75)
        self.driver.execute_script("window.scrollTo(0, 35000);")
        time.sleep(30)
        try:
            self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/div/div/div/a").click()
            altURL = self.driver.current_url
            self.getKeywords(altURL)
            self.getText(altURL)
        except:
            print('No reliable stories on topic. Further research advised.')

    def scrapePage(self, altURL=''):
        try:
            self.driver.current_url
        except:
            self.driver = webdriver.Chrome()

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
        finalText = ''.join(cleaned_text)
        return finalText

    def getKeywords(self, altURL=''):
        text = self.getText(altURL if altURL != '' else self.userURL)
        keywords = self.keywordGetter.find_keywords(text)
        if altURL == '':
            self.userKeywords = keywords
        else:
            self.trustedKeywords = keywords
        return keywords

    def getSentiment(self, altURL=''):
        text = self.getText(altURL if altURL != '' else self.userURL)
        sentiment = self.keywordGetter.analyze_sentiment(text)
        if altURL == '':
            self.userSentiment = sentiment
        else:
            self.trustedSentiment = sentiment
        return sentiment

    def compareKeywords(self):
        uKeywords = ''.join(self.userKeywords)
        tKeywords = ''.join(self.trustedKeywords)
        return self.keywordGetter.compare_keywords(uKeywords, tKeywords)

    def compareSentiment(self):
        return self.keywordGetter.compare_sentiment(self.userSentiment, self.trustedSentiment)


webscraper = WebScraper('https://www.foxnews.com/us/maryland-garbage-collector-shot-to-death-on-job-police-searching-suspects')
webscraper.searchTrustedPage()
print(webscraper.compareKeywords())
print(webscraper.compareSentiment())
