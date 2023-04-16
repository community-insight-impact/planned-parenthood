import re
from nltk.corpus import stopwords
import string
from collections import Counter

class TextProcessor:
    def __init__(self, input_corpus: list):
        self.processed_corpus = input_corpus

    def remove_digits(self):
        """Removes digits"""
        for index, row in enumerate(self.processed_corpus):
            self.processed_corpus[index] = re.sub("[0-9]+", " ", row)

    def remove_punctuation(self):
        """Removes punctuation"""
        for index, row in enumerate(self.processed_corpus):
            self.processed_corpus[index] = re.sub(r"[^\w\s]", " ", row)

    def remove_stop_words(self):
        """Removes stop words"""
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
            self.processed_corpus[index] = [
                token.lower()
                for token in row.split()
                if token.lower() not in stops
            ]

    def remove_common_words(self):
        """Removes the 20 most common words from the corpus"""
        counter = Counter([item for sublist in self.processed_corpus for item in sublist])
        most_common = [tuple[0] for tuple in counter.most_common(20)]
    
        for index, row in enumerate(self.processed_corpus):
            self.processed_corpus[index] = " ".join(
                [
                    token.lower()
                    for token in row
                    if token not in most_common
                ]
            )