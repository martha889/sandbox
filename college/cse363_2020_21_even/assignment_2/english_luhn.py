import os
import xml.etree.ElementTree as ET
import pandas as pd
import nltk
from matplotlib import pyplot as plt
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from operator import itemgetter
import string
import math


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
document_id = 0

tokenizer = RegexpTokenizer(r'[a-zA-Z]\w*')
token_count = {}

for book in corpus:
    path = cwd + "//" + book

    if os.path.isdir(path):
        for document in os.listdir(path):
            document_path = path + "//" + document

            try:
                tree = ET.parse(document_path)
                root = tree.getroot()
                text = ""

                for child in root:
                    if child.tag == "TEXT":
                        text += child.text

                text_cleaned = clean_text(text.lower())
                tokens = tokenizer.tokenize(text_cleaned)
                tokens = stopwords_removal(tokens)

                tokens = stemming(tokens)

                for token in tokens:
                    if token not in token_count:
                        token_count[token] = 1
                    else:
                        token_count[token] += 1

            except Exception as e:
                print(e)

            document_id += 1
            print("Document Number: ", document_id)


tokens_list = []

for token in token_count:
    tokens_list.append([token, token_count[token]])

dataframe = []

for token_row in tokens_list:
    dataframe.append([token_row[0], token_row[1]])

dataframe = sorted(dataframe, key=itemgetter(1), reverse=True)

graph_x_rank = []
graph_y_frequency = []

for i in range(10):
    graph_x_rank.append(i+1)
    graph_y_frequency.append(math.log(dataframe[i][1]))

plt.plot(graph_x_rank, graph_y_frequency, marker='o', markerfacecolor='red')
plt.title("Luhn's Law")

for i in range(10):
    plt.annotate(dataframe[i][0], (graph_x_rank[i], graph_y_frequency[i]))

plt.grid(True)
plt.xlabel("Rank")
plt.ylabel("log(frequency)")
plt.show()

df = pd.DataFrame(dataframe, columns=["Word", "Frequency"])
df.to_excel("luhn_english.xlsx")