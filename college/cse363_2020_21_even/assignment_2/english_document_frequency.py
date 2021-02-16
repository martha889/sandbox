import os
import xml.etree.ElementTree as ET
import nltk
import string
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from operator import itemgetter
import pandas as pd


def stopwords_removal(tokens_list):
    stopwords = nltk.corpus.stopwords.words('english')
    return [token for token in tokens_list if token not in stopwords]


def stemming(tokens_list):
    porter_stemmer = PorterStemmer()
    return [porter_stemmer.stem(token) for token in tokens_list]


def clean_text(text_string):
    return "".join([character for character in text if character not in string.punctuation])


cwd = os.getcwd() + "//English Dataset"

corpus = os.listdir(cwd)  # List of folder names

tokenizer = RegexpTokenizer(r'[a-zA-Z]\w*')  # Consider only words starting with alphabet


document_number = 0  # Document number: will be used to map file-name to a number
document_index = {}  # Map Document number to document name
data = {}  # of form {Document number: {Token: Count}} (dictionary of dictionary)

tokens_all = set()

for book in corpus:  # book is a folder containing documents
    path = cwd + "//" + book

    if os.path.isdir(path):  # If the path is of a folder
        for document in os.listdir(path):  # Iterate over documents in book
            document_path = path + "//" + document

            try:
                tree = ET.parse(document_path, ET.XMLParser(encoding='utf-8'))
                root = tree.getroot()
                text = ""  # Returns the text between <TEXT> tag of the documents
                for child in root:
                    if child.tag == "TEXT":
                        text += child.text

                text_cleaned = clean_text(text.lower())  # Convert to lowercase and remove punctuations
                tokens = tokenizer.tokenize(text_cleaned)
                tokens = stopwords_removal(tokens)
                tokens = stemming(tokens)

                tokens_set = set(tokens)  # Get unique tokens
                tokens_all = tokens_all.union(tokens_set)  # Add tokens of this document to all tokens

                document_dict = {}  # Dictionary containing tokens in a document, mapped to their count

                for token in tokens:
                    if token not in document_dict:
                        document_dict[token] = 1
                    else:
                        document_dict[token] += 1

                document_index[document_number] = document  # Map names of documents in a dictionary to numbers

                data[document_number] = document_dict

            except Exception as e:
                print(e)

            document_number += 1
            print("Document Number:", document_number)  # 39,000+ Documents (will indicate progress)


postings_list = {}
token_frequency = {}  # {Token: Count} (dictionary)


for doc_id in data:
    for token in data[doc_id]:
        if token not in token_frequency:
            token_frequency[token] = 1
        else:
            token_frequency[token] += data[doc_id][token]
        if token not in postings_list:
            postings_list[token] = [doc_id]
        else:
            postings_list[token].append(doc_id)


print("B")
print("Number of tokens: ", len(tokens_all))
token_no = 1
tokens_dict = {}

for token in tokens_all:
    print("Token Number: ", token_no)
    if token not in tokens_dict:
        tokens_dict[token] = []

    for doc_id in data:
        if token in data[doc_id]:
            tokens_dict[token].append([doc_id, data[doc_id][token]])
    token_no += 1
print("C")

dataframe = [[token, tokens_dict[token]] for token in tokens_dict]
dataframe = sorted(dataframe, key=itemgetter(0))

print("D")

df = pd.DataFrame(dataframe, columns=["Token", "[Doc ID, Doc Frequency]"])
df.to_excel("english_doc_frequency.xlsx")

print("E")