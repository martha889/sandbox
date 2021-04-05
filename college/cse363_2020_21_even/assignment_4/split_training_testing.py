"""Split training and testing data
How? Put training files in separate folders as per class
Put testing files all in a single folder"""

import os
import shutil
import random

TRAIN_TEST_SPLIT = 45  # % of data to be used as training data

path = os.getcwd()

training_path = path + "\\training_data"
testing_path = path + "\\testing_data"

try:
    os.mkdir(training_path)
    os.mkdir(testing_path)
except Exception as e:
    print(e)

class_list = path + "\\20_newsgroups"

for class_name in os.listdir(class_list):
    class_path = class_list + "\\" + class_name

    try:
        os.mkdir(training_path + "\\" + class_name)  # Make folder if not there, else do nothing
    except Exception as e:
        print(e)

    list_of_files = os.listdir(class_path)
    random.shuffle(list_of_files)

    split_point = TRAIN_TEST_SPLIT * len(list_of_files) // 100
    training_files = list_of_files[:split_point]
    testing_files = list_of_files[split_point:]

    total_training = len(training_files)
    total_testing = len(testing_files)
    count = 1

    for file in training_files:
        print("Training file " + str(count) + " out of " + str(total_training))
        count += 1
        shutil.copyfile(class_path + "\\" + file, training_path + "\\" + class_name + "\\" + file)

    count = 1

    for file in testing_files:
        print("Testing file " + str(count) + " out of" + str(total_testing))
        count += 1
        shutil.copyfile(class_path + "\\" + file, testing_path + "\\" + file)


