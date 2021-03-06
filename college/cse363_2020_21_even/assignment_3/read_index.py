"""Read JSON files as dictionaries"""

import json

with open("saved_postings_dict.json") as f:
    postings_dict = json.load(f)
    f.close()

with open("saved_term_frequency.json") as f:
    term_frequency = json.load(f)
    f.close()

with open("saved_document_frequency.json") as f:
    document_frequency = json.load(f)
    f.close()

with open("saved_document_map.json") as f:
    document_map = json.load(f)
    f.close()

"""Reminder: term_frequency: {document-name: {token: count(in that document)}}"""
document_number = len(term_frequency.keys())  # total number of documents. Needed for idf term.
