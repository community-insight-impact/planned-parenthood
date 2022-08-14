import re
from nltk.corpus import stopwords
import string


class TextProcessor:
    def __init__(self, input_corpus: list):
        self.processed_corpus = input_corpus

    def remove_digits(self):
        """Removes the digits in the description"""
        for index, row in enumerate(self.processed_corpus):
            self.processed_corpus[index] = re.sub("[0-9]+", " ", row)

    def remove_punctuation(self):
        """Removes punctuation from the description"""
        for index, row in enumerate(self.processed_corpus):
            self.processed_corpus[index] = re.sub(r"[^\w\s]", " ", row)

    def remove_stop_words(self):
        stops = set(stopwords.words('english'))
        words_to_keep = [
            "shan",
            "couldn",
            "against",
            "shouldn",
            'can',
            "needn",
            'should',
            'not',
            "mustn",
            'will'
        ]
        for keep in words_to_keep:
            stops.remove(keep)
        
        stops = list(stops)
        stops += list(string.ascii_lowercase)
        stops += ['ii', 'iii', 'iv']

        for index, row in enumerate(self.processed_corpus):
            self.processed_corpus[index] = " ".join(
                token.lower()
                for token in row.split()
                if token.lower() not in stops
            )