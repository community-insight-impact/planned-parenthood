import pandas as pd
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline

class NmfModel:
    """The model is a pipeline of TF-IDF Vectorizer and Non-negative Matrix Factorization"""
    def __init__(self):
        self.model = make_pipeline(
            TfidfVectorizer(
                ngram_range=(1,2), 
                lowercase=False, 
                stop_words=None
            ),
            NMF(n_components=10, random_state=0)
        )
        self.transformed_data = None

    def fit_model(self, X: list):
        """Fits and transform model given input

        Parameters
        ----------
        X : list
            list of processed policies
        """
        self.transformed_data = self.model.fit_transform(X)

    def get_words_from_topic(self):
        """Gets the top 10 words with the highest value from each topic"""
        components_df = pd.DataFrame(
            self.model[1].components_, 
            columns=self.model[0].get_feature_names_out()
        )

        for idx, row in components_df.iterrows():
            print(f'For topic {idx+1}, the words with the highest value are:')
            print(row.nlargest(10))
    
    def get_documents_topic(self):
        """Get all of the documents' topics"""
        document_order = self.transformed_data.argmax(1) + 1
        pd.DataFrame(
            document_order
        ).to_csv("../data/documents_topic.csv")