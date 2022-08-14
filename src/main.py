from text_processor import TextProcessor

def main():
    with open('../policies/2.txt', encoding="ascii", errors="ignore") as f:
        contents = f.readlines()
    processing_instance = TextProcessor(contents)
    processing_instance.remove_digits()
    processing_instance.remove_punctuation()
    processing_instance.remove_stop_words()
    processing_instance

if __name__ == "__main__":
    main()