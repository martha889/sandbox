import os
import text_processing
import json
import time

start_time = time.time()

class_list = os.getcwd() + "\\training_data"

master_dict = {}  # {class-name(=folder name): class dictionary(={token:count})}

folder_count = 0  # To show progress
folder_total = len(os.listdir(class_list))

probability_class_dict = {}

for folder in os.listdir(class_list):
    folder_count += 1

    folder_path = class_list + "\\" + folder

    class_dict = {}  # Store {token: count}

    master_dict[folder] = class_dict

    print("Folder path:", folder_path)

    file_count = 1  # To show progress
    file_total = len(os.listdir(folder_path))

    probability_class_dict[folder] = (file_total / 16810)  # Get total file count through explorer

    for file in os.listdir(folder_path):
        print("File ", str(file_count) + " out of " + str(file_total), end="; ")
        print("Folder ", str(folder_count) + " out of " + str(folder_total))
        file_count += 1

        file_path = folder_path + "\\" + file

        f = open(file_path, 'r')

        text_body = f.read()
        token_list = text_processing.text_processing(text_body)  # Token list for all tokens in a file

        for token in token_list:
            if token not in class_dict:
                class_dict[token] = 1
            else:
                class_dict[token] += 1


end_time = time.time()
print("Training time: ", end_time - start_time)

with open("saved_master_dict.json", 'w') as f:
    json.dump(master_dict, f)
    f.close()

with open("saved_probability_class_dict.json", 'w') as f:
    json.dump(probability_class_dict, f)
    f.close()