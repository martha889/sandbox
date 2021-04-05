import json
import os
import text_processing
from math import log2, inf

with open("saved_master_dict.json") as f:
    master_dict = json.load(f)
    f.close()

with open("saved_probability_class_dict.json") as f:
    probability_class_dict = json.load(f)
    f.close()

testing_data = os.getcwd() + "\\testing_data"

result_dict = {}
list_of_classes = list(master_dict.keys())


def class_map_calculation(list_tokens, class_name):
    """Return c_map calculation for a certain class"""
    total = log2(probability_class_dict[class_name])

    total_count = sum(master_dict[class_name].values())

    for token in list_tokens:
        try:
            probability = (master_dict[class_name][token] + 1) / (total_count + len(master_dict.keys()))
        except KeyError:  # Document has a word that is not in the given class
            probability = 1 / (total_count + len(master_dict.keys()))
        total += log2(probability)

    return total


total_files = len(os.listdir(testing_data))
count_file = 1

for file in os.listdir(testing_data):
    print("File " + str(count_file) + " out of " + str(total_files))
    count_file += 1

    file_path = testing_data + "\\" + file

    f = open(file_path, 'r')
    text_body = f.read()
    token_list = text_processing.text_processing(text_body)

    best_score = -inf
    best_class = None

    for name in list_of_classes:
        score = class_map_calculation(token_list, name)

        if score > best_score:
            best_score = score
            best_class = name

    result_dict[file] = best_class

with open("saved_result_dict.json", 'w') as f:
    json.dump(result_dict, f)
    f.close()
