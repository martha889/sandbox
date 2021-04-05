By: Sarthak Choudhary (17085066) and Prahlad Chaudhary (17085054)

Notes:

1. The code is divided into the following files:

	a) training.py -> reads the \training_data folder and saves the following files:
		1) saved_master_dict.json -> Store the term count for every class in the training data. Format (nested dictionary): {class-name: {term: count}}.
		2) saved_probability_class_dict.json -> store probability of selecting each class, i.e. (number of files in a class / total number of files). Format (dictionary): {class-name: probability}.
	
	b) testing.py -> reads the \testing_data folder and saves the following file:
		1) saved_result_dict.json -> store the result, i.e. {file-name: predicted-class}
		
	c) Additional files:
		1) split_training_testing.py -> Used to randomly divide the data into training and testing data. Default split ratio = 60:40;
		2) labeled_data.py -> reads the \20_newsgroups folder and saves the correct labelling of every file in saved_labeled_data.json file
		3) check_accuracy.py -> Compares results of saved_result_dict.json with saved_labeled_data.json and outputs the percentage of correct predictions in the testing data.
		4) text_processing.py -> Used for stopword removal and tokenization. 
		
		
2. How to run the code?

	External library required: nltk (for stopword removal, stemming using Porter stemmer)
	Link for dataset (original 20 newsgroups datasets): http://qwone.com/~jason/20Newsgroups/20news-19997.tar.gz
	
	1) Ensure that the \20_newsgroups folder is in the same directory as all the *.py files. 
	2) Run split_training_testing.py. It will create two folders: \testing_data and \training_data.
	2) Run training.py
	3) Run testing.py 
	4) run check_accuracy.py
	
	5) Modify and rerun: delete \testing_data and \training_data folders and repeat from step 2. (Created *.json files are automatically overwritten)
	
3. Observations/Results:
	1) The following accuracies as per split ratio were obtained:
		a) 80:20 -> 75.35%
		b) 70:30 -> 75.66%
		c) 60:40 -> 77.24%
		d) 50:50 -> 78.63%
		e) 40:60 -> 76.55%