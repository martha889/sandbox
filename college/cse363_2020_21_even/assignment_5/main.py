from bs4 import BeautifulSoup
from urllib.request import urlopen
from queue import Queue

HOMEPAGE = 'https://en.wikipedia.org'
number_of_pages = 1000  # pages to crawl

queue = Queue()  # Queue object allows O(1) insertion/deletion from queue (URL frontier)
queue.put('https://en.wikipedia.org/wiki/Information_retrieval')  # Start page

crawled = set()

with open("crawled.txt", 'w', encoding='utf-8') as file:  # Create file to write the URLS of crawled pages to.
    file.close()

while queue.qsize() and number_of_pages:  # While there are links in the queue
    page_url = queue.get()
    response = urlopen(page_url)
    print("Crawling page:", page_url)
    soup = BeautifulSoup(response, 'lxml')

    with open ("crawled.txt", 'a') as file:
        file.write(page_url + "\n")

    for a in soup.find_all('a', href=True):  # Find all links under href attribute of <a> tag
        link = a['href']
        output_url = ''

        if link.startswith('/wiki'):  # Convert relative link to absolute link
            output_url += HOMEPAGE + link

        elif link.startswith('https://en.wikipedia.org'):  # only crawl the English wikipedia website
            output_url += link

        if len(output_url) and page_url not in crawled:  # Avoid duplicates and empty strings
            queue.put(output_url)  # Only store absolute links in queue

    crawled.add(page_url)
    number_of_pages -= 1