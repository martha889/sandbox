By: Sarthak Choudhary (17085066) and Prahlad Chaudhary (17085054)

Notes:

1. The code is divided into the following files:

	a) training.py -> reads the \training_data folder and saves the following files:
		1) saved_master_dict.json -> Store the term count for every class in the training data. Format (nested dictionary): {class-name: {term: count}}.
		2) saved_probability_class_dict.json -> store probability of selecting each class, i.e. (number of files in a class / total number of files). Format (dictionary): {class-name: probability}.
	
	b) testing.py -> reads the \testing_data folder and saves the following file:
		1) saved_result_dict.json -> store the result, i.e. {file-name: predicted-class}
		
	c) Additional files:
		1) split_training_testing.py -> 
		2) check_accuracy.py -> 
		3) text_processing.py -> 
		
2. How to run the code?

	External library required: nltk (for stopword removal, stemming using Porter stemmer)
	
	Link for dataset (original 20 newsgroups datasets): http://qwone.com/~jason/20Newsgroups/20news-19997.tar.gz
	
3. Comments/Observations