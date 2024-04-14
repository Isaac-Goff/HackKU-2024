from rake_nltk import Rake
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class CompareWebsites:

    def __init__(self):
        self.rake = Rake()
        self.text = ''
        self.analyzer = SentimentIntensityAnalyzer()

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    def find_keywords(self, text):

        self.rake.extract_keywords_from_text(text)
        keywords = self.rake.get_ranked_phrases()
        return keywords

    def process_text(self, text):
        tokens = word_tokenize(text)
        filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]

        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
        processed_text = ' '.join(lemmatized_tokens)
        return processed_text

    def analyze_sentiment(self, text):
        processed_text = self.process_text(text)
        scores = self.analyzer.polarity_scores(processed_text)
        sentiment = 1 if scores['pos'] > 0 else 0
        return scores

    def compare_keywords(self, website_text, reliable_text):
        score = 0
        website_keywords = self.find_keywords(website_text)
        reliable_keywords = self.find_keywords(reliable_text)
        for webword in website_keywords:
            if webword in reliable_keywords:
                score += 1

        percent_score = (score / len(website_keywords)) * 100
        return score,len (website_keywords), percent_score

    def compare_sentiment(self, website_text, reliable_text):
        scores = {}
        website_sentiment = self.analyze_sentiment(website_text)
        reliable_sentiment = self.analyze_sentiment(reliable_text)

        for key in website_sentiment:
            scores[key] = 100 - abs(round(website_sentiment[key] - reliable_sentiment[key], 4) * 100)
        return scores


textList = ['You can form a powerful keyword extraction method by '
            'combining the Rapid Automatic Keyword Extraction (RAKE) '
            'algorithm with the NLTK toolkit. It is known as rake-nltk. '
            'It is a modified version of this algorithm. You can know '
            'more about rake-nltk here.Install the rake-nltk library '
            'using pip install rake-nltk.',
            'First, we’ll import the necessary libraries for text analysis and '
            'sentiment analysis, such as pandas for data handling, nltk for '
            'natural language processing, and SentimentIntensityAnalyzer for '
            'sentiment analysis.']
sentimentAnalyser = CompareWebsites()

