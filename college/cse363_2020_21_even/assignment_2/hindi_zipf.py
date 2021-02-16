import os
import xml.etree.ElementTree as ET
import pandas as pd
from matplotlib import pyplot as plt
from operator import itemgetter
import math
from string import punctuation


def tokenize(text_string):  # Remove punctuations and tokenize
    new_string = ""
    for character in text_string:

        if character not in (punctuation + "।"):
            new_string += character

    new_string = new_string.split()

    return new_string


cwd = os.getcwd() + "//Hindi Dataset"
book = os.listdir(cwd)  # List of folder names

token_count = {}
document_no = 0

print("Number of documents: ", len(book))

for document in book:
    document_path = cwd + "//" + document

    if os.path.isfile(document_path):

        try:
            tree = ET.parse(document_path)
            root = tree.getroot()
            text = ""

            for child in root:
                if child.tag == "TEXT":
                    text += child.text

            text_tokenized = tokenize(text)

            for token in text_tokenized:
                if token not in token_count:
                    token_count[token] = 1
                else:
                    token_count[token] += 1

            print(document_no)
            document_no += 1

        except Exception as e:
            print(e)

tokens_list = []

for token in token_count:
    tokens_list.append([token, token_count[token]])

dataframe = []

for token_row in tokens_list:
    dataframe.append([token_row[0], token_row[1]])

dataframe = sorted(dataframe, key=itemgetter(1), reverse=True)
print(dataframe[:100])

graph_x_rank = []
graph_y_frequency = []

for i in range(10):
    graph_x_rank.append(i+1)
    graph_y_frequency.append(math.log(dataframe[i][1]))

plt.rcParams["font.family"] = "Devanagari"

plt.plot(graph_x_rank, graph_y_frequency, marker='o', markerfacecolor='red')
plt.title("Zipf's Law")


for i in range(10):
    plt.annotate(dataframe[i][0], (graph_x_rank[i], graph_y_frequency[i]))

plt.grid(True)
plt.xlabel("Rank")
plt.ylabel("log(frequency)")
plt.show()

df = pd.DataFrame(dataframe, columns=["Word", "Frequency"])
df.to_excel("zipf_hindi.xlsx")