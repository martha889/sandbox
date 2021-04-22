By: Sarthak Choudhary (17085066) and Prahlad Chaudhary (17085054)

Notes:

*  External libraries required: BeatifulSoup (used to extract links from href attribute of the anchor tag), lxml (parser)
*  A queue object is used to store the URLs of the pages that are yet to be crawled.

The program does the following:

1. Add the start page to the queue  ("https://en.wikipedia.org/wiki/Information_retrieval" used)
2. Use the built-in urllib.request module to send an http request to the first page in the queue
3. Gather all links under href attribute of the anchor tag and add them to the queue
4. Remove the page from the queue 
5. Add the URL of the crawled page to crawled.txt
6. Go back to step 2, or stop if the queue is empty or a given number of pages have been crawled. 