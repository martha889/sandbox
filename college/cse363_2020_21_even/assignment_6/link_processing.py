def generate_output_url(link, homepage='https://en.wikipedia.org'):
    output_url = ''

    if link.startswith('/wiki'):  # Convert relative link to absolute link
        output_url += homepage + link

    elif link.startswith('https://en.wikipedia.org'):  # only crawl the English wikipedia website
        output_url += link

    return output_url
