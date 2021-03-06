By: Sarthak Choudhary (17085066) and Prahlad Chaudhary (17085054)

Notes:

1. The code is divided into the following files for convenience and readability: (the files which may be needed to run are starred)

	a) * create_index.py -> Does the required processing on database and saves the needed data in .json format. The files are in the format "saved_...".json. Comments added in the file for detailed explanation.
	b) read_index.py -> Simply loads the saved json files and saves them as dictionary (type) variables.
	c) text_processing.py -> Contains functions for stopword removal, stemming, punctuation removal, tokenization.
	d) boolean_operators.py -> Contains AND, OR, NOT operators. Used for Boolean Retrieval.
	e) * boolean_retrieval.py -> Contains the code for Boolean Retrieval Model.
	f) * vector_space_model.py -> Contains the code for Vector Space Model.
	
	NOTE: For Hindi, files have the same name prefixed by "hindi_". Example: hindi_create_index.py. Most of the code is same. Only the text_processing file is different due to different requirements for stemming, stopword removal. 
   
2. How to run the code?

	External library required: nltk (for stopword removal, stemming using Porter stemmer)
	
	** The code requires .json files (created index). If you don't have them, make sure you have he database "English Dataset"  "Hindi Dataset".
	Link for datasets: 
	English: https://drive.google.com/file/d/1FnURJo6OQuHLjj-_M6lY5VvoFbbssxQd/view?usp=sharing
	Hindi: https://drive.google.com/file/d/10brF5db4DlidRTSbUUg_Zm6ARS1SChmK/view?usp=sharing
	
	a) Make sure you have the index .json files (prefixed by "saved_ or hindi_saved_") in the same folder as the .py files. 
	b) If you don't have the .json files, make sure the 'English Dataset' folder and/or 'Hindi Dataset' folder is in the same folder and run the create_index.py file. It will create the index (.json files) for you. 
	
	c) Run the respective IR model file, i.e. boolean_retrieval.py or vector_space_model.py and entery your query. 
	
3. Comments/Observations
	a) Good results were obtained (the search query was almost always found especially if it was a longer query).
	b) It was observed that the vector space model did not consider the order of the relevant terms, it just counted the relevant terms. If the query was "hello hello is there anybody", a document which had the exact phrase sometimes did not have a higher score than the one which had all of the tokens but not in the correct order. 
	
 
 