from rake_nltk import Rake
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class SentimentAnalyst:

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
        print(keywords)

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
        return sentiment



sentimentAnalyser = SentimentAnalyst()
sentimentAnalyser.find_keywords('You can form a powerful keyword extraction method by '
                                'combining the Rapid Automatic Keyword Extraction (RAKE) '
                                'algorithm with the NLTK toolkit. It is known as rake-nltk. '
                                'It is a modified version of this algorithm. You can know '
                                'more about rake-nltk here.Install the rake-nltk library '
                                'using pip install rake-nltk.')
print(sentimentAnalyser.analyze_sentiment('You can form a powerful keyword extraction method by '
                                'combining the Rapid Automatic Keyword Extraction (RAKE) '
                                'algorithm with the NLTK toolkit. It is known as rake-nltk. '
                                'It is a modified version of this algorithm. You can know '
                                'more about rake-nltk here.Install the rake-nltk library '
                                'using pip install rake-nltk.'))