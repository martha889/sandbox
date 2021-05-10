import json
import numpy as np
from text_processing import *

with open("saved_web_graph_dict.json") as f:
    web_graph_dict = json.load(f)
    f.close()

with open("saved_term_index.json") as f:
    term_index = json.load(f)
    f.close()

query = input("Enter your query (related to information retrieval): ")
query_tokens_list = text_processing(tokenize(query))  # Use functions from text_processing.py to return list of tokens

root_set = []
hits_web_graph_dict = {}  # Adjacency list

set_pages = set()  # To avoid adding duplicate pages in base set and root set

for token in query_tokens_list:
    try:
        pages_contain_token = term_index[token]

        for page in pages_contain_token:
            if page not in set_pages:
                set_pages.add(page)
                root_set.append(page)

    except KeyError:  # KeyError may arise due to misspellings
        pass

"""Build base set"""

base_set = root_set.copy()

# Add out-links from every page in the root set
for source_page in root_set:
    try:
        out_links = web_graph_dict[source_page]

        for destination_page in out_links:
            if destination_page not in set_pages:
                set_pages.add(destination_page)
                base_set.append(destination_page)

    except KeyError:  # Page may not have any out-links, but may have only in-links.
        pass


# Add in-links to every page in the root set
for destination_page in root_set:
    for source_page in web_graph_dict.keys():
        try:
            if destination_page in web_graph_dict[source_page] and source_page not in set_pages:
                set_pages.add(source_page)
                base_set.append(source_page)

        except KeyError:  # Page may have out-links and no in-links
            pass

number_of_pages = len(base_set)

adjacency_matrix = np.zeros((number_of_pages, number_of_pages))

for i in range(len(base_set)):
    source_page = base_set[i]

    for j in range(len(base_set)):
        destination_page = base_set[j]

        try:
            if destination_page in web_graph_dict[source_page]:
                adjacency_matrix[i][j] = 1
        except KeyError:  # Reason same as the previous KeyError exception
            pass

A_AT = np.matmul(adjacency_matrix, adjacency_matrix.T)
AT_A = np.matmul(adjacency_matrix.T, adjacency_matrix)

hub_scores, authority_scores = np.ones(number_of_pages).T, np.ones(number_of_pages).T

lambda_h = np.round(max(np.linalg.eigvals(A_AT)))
lambda_a = np.round(max(np.linalg.eigvals(AT_A)))

for _ in range(50):
    hub_scores = (1 / lambda_h) * np.matmul(A_AT, hub_scores)
    authority_scores = (1 / lambda_a) * np.matmul(AT_A, authority_scores)

hub_scores = abs(hub_scores)
authority_scores = abs(authority_scores)  # abs done to use change complex number values to their modulus

hub_index = [[i, hub_scores[i]] for i in range(len(hub_scores))]
authority_index = [[i, authority_scores[i]] for i in range(len(authority_scores))]

hub_index.sort(reverse=True, key=lambda x: x[1])
authority_index.sort(reverse=True, key=lambda x: x[1])

hub_ranking = [[base_set[i[0]], i[1]] for i in hub_index]  # [page-name, hub-score]
authority_ranking = [[base_set[i[0]], i[1]] for i in authority_index]  # [page-name, authority-score]

count = 0  # We need to output only top 10 pages, so we count them using this variable.
print("Ranking of hubs: ")
for hub in hub_ranking:
    print("Hub name: ", hub[0], ", Hub score: ", hub[1])
    count += 1
    if count == 10:
        break

count = 0
print()
print("Ranking of authorities: ")
for authority in authority_ranking:
    print("Authority name: ", authority[0], ", Authority score: ", authority[1])
    count += 1
    if count == 10:
        break
