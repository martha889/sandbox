import json
import numpy as np

ALPHA = 0.1  # Teleportation probability

with open("saved_web_graph_dict.json") as f:
    web_graph_dict = json.load(f)
    f.close()


list_of_pages = list(web_graph_dict.keys())  # Use for indexing
STARTING_PAGE = list_of_pages[0]
number_of_pages = len(list_of_pages)

adjacency_matrix = np.zeros((number_of_pages, number_of_pages))
probability_matrix = np.zeros((number_of_pages, number_of_pages))

for i in range(len(list_of_pages)):
    source_page = list_of_pages[i]

    for j in range(len(list_of_pages)):
        destination_page = list_of_pages[j]

        if destination_page in web_graph_dict[source_page]:
            adjacency_matrix[i][j] = 1


for row_number in range(len(adjacency_matrix)):
    number_of_zeros = np.count_nonzero(adjacency_matrix[row_number])

    probability_matrix[row_number] = adjacency_matrix[row_number] / (number_of_zeros if number_of_zeros > 0 else 1)


probability_matrix *= (1 - ALPHA)
probability_matrix += (ALPHA / number_of_pages)

position_matrix = np.zeros((1, number_of_pages))
position_matrix[0][0] = 1  # Starting position = 1st page

NUMBER_OF_STEPS = 2

for _ in range(NUMBER_OF_STEPS):
    position_matrix = np.matmul(position_matrix, probability_matrix)

score_dictionary = {}

for i in range(len(list_of_pages)):
    page = list_of_pages[i]
    score_dictionary[page] = position_matrix[0][i]

list_of_pages.sort(key=lambda x: score_dictionary[x], reverse=True)

for page in list_of_pages:
    print(f"Page: {page}; PageRank Score: {score_dictionary[page]}")


