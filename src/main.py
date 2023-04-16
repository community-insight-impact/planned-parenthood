from text_processor import TextProcessor
from os import listdir
from nmf_model import NmfModel
import re

def main():
    policy_contents = []
    document_order = []
    for f in listdir('../policies'):
        with open('../policies/' + f, encoding="ascii", errors="ignore") as f:
            contents = f.read()
            policy_contents.append(contents)
        document_order.append(re.split("[^\w\s]", f.name)[4])

    processing_instance = TextProcessor(policy_contents)
    processing_instance.remove_digits()
    processing_instance.remove_punctuation()
    processing_instance.remove_stop_words()
    processing_instance.remove_common_words()
    
    model = NmfModel()
    model.fit_model(processing_instance.processed_corpus)
    model.get_words_from_topic()
    model.get_documents_topic()

if __name__ == "__main__":
    main()