"""Crawl pages given a starting page. Build a web-graph and save it as JSON"""

import json
import text_processing
from bs4 import BeautifulSoup
from link_processing import *
from urllib.request import urlopen
from queue import Queue

number_of_pages = 200  # pages to crawl

term_index = {}

queue = Queue()  # Queue object allows O(1) insertion/deletion from queue (URL frontier)
queue.put('https://en.wikipedia.org/wiki/Information_retrieval')  # Start page

web_graph_dict = {}  # adjacency list

crawled = set()

while queue.qsize() and number_of_pages:  # While there are links in the queue
    page_url = queue.get()
    if page_url not in crawled:
        response = urlopen(page_url)
        print("Number of pages left:", number_of_pages)
        print("Crawling page: ", page_url)
        soup = BeautifulSoup(response, 'lxml')

        if page_url not in web_graph_dict:
            web_graph_dict[page_url] = []

        for a in soup.find_all('a', href=True):  # Find all links under href attribute of <a> tag
            link = a['href']
            text = a.string  # Anchor text
            output_url = generate_output_url(link)

            if len(output_url) and (output_url not in crawled) and not output_url.count('#') and output_url.count(':') == 1 and text is not None:  # Avoid duplicates and empty strings
                web_graph_dict[page_url].append(output_url)
                queue.put(output_url)  # Only store absolute links in queue

                tokens_list = text_processing.tokenize(text)
                tokens_list = text_processing.text_processing(tokens_list)

                for term in tokens_list:
                    if term not in term_index:
                        term_index[term] = [output_url]
                    else:
                        term_index[term].append(output_url)

        crawled.add(page_url)
        number_of_pages -= 1

with open("saved_web_graph_dict.json", 'w') as f:
    json.dump(web_graph_dict, f)
    f.close()

with open("saved_term_index.json", 'w') as f:
    json.dump(term_index, f)
    f.close()

print(web_graph_dict.keys())