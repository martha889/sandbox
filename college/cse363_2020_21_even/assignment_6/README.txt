By: Sarthak Choudhary (17085066) and Prahlad Chaudhary (17085054)

Notes:

* We've taken the starting page as the wikipedia page of information retrieval, i.e. 'https://en.wikipedia.org/wiki/Information_retrieval'.
* Our collection consists of 400 pages, beginning from the above starting page.
* The query for the HITS algorithm can be anything related to information retrieval.


Ex
1. The code is divided into the following files:

** Auxiliary Files:

    a) text_processing.py -> Contains functions to tokenize a body of text, do stemming and stop word removal.
    b) link_processing.py -> Contains functions to change relative links to absolute links. Also makes sure that only the links of 'en.wikipedia.org' are followed.


** Main files:
    a) create_index.py -> Add a starting page to the queue. While the queue is not empty or the number of pages have not been visited,
                          keep adding all the links in the page to the queue. Repeat for the next page in the queue.

                          For each page, we do some computations which result in the following two files:

                          1. saved_web_graph_dict.json -> An adjacency list representation of graph. Format: {page-url: list of out-links from page-url}
                          2. saved_term_index.json -> Term index for each term formed by using the anchor text of each link (stemming, stopword removal also done). Format: {term: list of pages whose anchor text contain that term}

    b) page_rank.py -> Loads the graph (using saved_web_graph_dict.json) and computes the PageRank scores for each page. Prints the pages in decreasing order of score.

    c) hits_algorithm_query.py -> Loads both the graph and the term index (using both saved files).
                                  Takes in a user query, builds the root set and base set as per the HITS algorithm.
                                  Returns both hub scores and authority scores for pages in the base set (ranked in decreasing order of scores).

*** How to run the code?
    External libraries required:

    a) nltk -> used in text_processing.py for stop word removal and stemming (Porter Stemmer).
    b) BeautifulSoup -> Used in create_index.py for extracting anchor text and link URLs.
    c) numpy -> used in page_rank.py for doing matrix calculations for computing probability matrix and position matrix.

    Running the code:

    a) If saved_term.json, saved_web_graph_dict.json are not present. Run create_index.py to create them.
    b) Run either page_rank.py or hits_algorithm_query.py.


