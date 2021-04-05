import string
import nltk
from nltk.stem.porter import PorterStemmer

stopwords = nltk.corpus.stopwords.words('english')
stemmer = PorterStemmer()


def text_processing(text_body):
    """Remove punctuations and stopwords.
    Since stopwords contain words like you'll, she's, etc., we first remove stopwords then remove punctuations
    Finally do stemming and return the tokenized list"""

    tokens_list = text_body.lower().split()

    tokens_list_new = []

    for token in tokens_list:
        if token not in stopwords and len(token):  # Remove empty string too
            new_token = ""
            for character in token:
                if character not in string.punctuation:
                    new_token += character

            tokens_list_new.append(stemmer.stem(new_token))

    return tokens_list_new