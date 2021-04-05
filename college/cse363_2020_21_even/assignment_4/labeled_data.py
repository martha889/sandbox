"""Label data with correct labels to check the accuracy of the algorithm
Create dictionary with correct labels: {document-name: class}
Assumption: all files have unique names"""

import os
import json

labeled_data_dict = {}

class_list = os.getcwd() + "\\20_newsgroups"

for folder in os.listdir(class_list):
    folder_path = class_list + "\\" + folder

    for file_name in os.listdir(folder_path):
        labeled_data_dict[file_name] = folder

with open("labeled_data_dict.json", 'w') as f:
    json.dump(labeled_data_dict, f)
    f.close()




