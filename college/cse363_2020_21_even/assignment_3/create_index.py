"""Create and save the following as JSON files:

document_map -> dictionary that maps document number to document path. Eg: 1 -> 'C:\\..\\en.13.10.11.2009.7.29'
document_frequency -> counts the frequency of each token in various documents (useful for tf-idf weight formula)
postings_dict -> inverted index for all tokens
term_frequency -> stores token count for every document in a nested dictionary. Format: {document-name: {token: count}}

"""
import os
import xml.etree.ElementTree as ET
import json

import text_processing

document_map = {}
token_count_dict = {}
postings_dict = {}

term_frequency = {}  # tf-idf weighing
document_frequency = {}  # tf-idf weighing

document_number = 0

cwd = os.getcwd() + "\\English Dataset"
corpus = os.listdir(cwd)

for book in corpus:
    path = cwd + "\\" + book

    if os.path.isdir(path):
        for document in os.listdir(path):

            document_path = path + "\\" + document

            try:
                tree = ET.parse(document_path)
                root = tree.getroot()

                """Map document number to document name"""
                document_map[document_number] = document_path

                title = ""
                text = ""

                for child in root:
                    if child.tag == "TEXT":
                        text += child.text
                    if child.tag == "TITLE":
                        title += child.text

                body = (title + text)  # Merge both title and body text in a single string
                tokens_list = text_processing.text_processing(text_processing.tokenize(body))  # Convert to lowercase, remove stopwords and punctuations, tokenize

                term_frequency_token_count = {}
                term_frequency_token_weight = {}

                for token in tokens_list:  # Document numbers added in increasing order (sorted)
                    if token not in postings_dict:
                        postings_dict[token] = [document_number]
                    else:
                        if postings_dict[token][-1] != document_number:  # don't add if already added
                            postings_dict[token].append(document_number)

                    if token not in token_count_dict:
                        token_count_dict[token] = 1
                    else:
                        token_count_dict[token] += 1

                    """tf-idf weighing"""

                    if token not in term_frequency_token_count:
                        term_frequency_token_count[token] = 1
                    else:
                        term_frequency_token_count[token] += 1

                    term_frequency[document_number] = term_frequency_token_count

                document_number += 1
                print("Document number: ", document_number)

            except Exception as e:
                print(e)

for term in postings_dict:
    document_frequency[term] = len(postings_dict[term])

"""Write the required data as .json. JSON used as it stores the type i.e. lists or dictionary can 
directly be loaded in their respective types """

with open("saved_postings_dict.json", 'w') as f:
    json.dump(postings_dict, f)
    f.close()

with open("saved_term_frequency.json", 'w') as f:
    json.dump(term_frequency, f)
    f.close()

with open("saved_document_frequency.json", 'w') as f:
    json.dump(document_frequency, f)
    f.close()

with open("saved_document_map.json", 'w') as f:
    json.dump(document_map, f)
    f.close()
