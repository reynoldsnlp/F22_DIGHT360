"""Iteratively scrape reynoldsnlp.com/scrape/."""

from glob import glob
import os
import sys
import time

from bs4 import BeautifulSoup
import requests

try:
    os.mkdir('scrape')  # Create the `scrape` directory
except FileExistsError:
    pass  # If it already exists, do nothing


def get_reynoldsnlp(filename):
    """Scrape html file from reynoldsnlp.com/scrape/; write to file."""
    # time.sleep(1)
    print(f'Requesting {filename}....')
    headers = {'user-agent': 'Robert Reynolds (robert_reynolds@byu.edu)'}
    response = requests.get('http://reynoldsnlp.com/scrape/' + filename,
                            headers=headers)
    with open('scrape/' + filename, 'w') as html_file:
        html_file.write(response.text)


def get_hrefs(filename):
    """Return list of href values from all <a> tags in `filename`."""
    assert filename.endswith('.html')
    print(f'Extracting hrefs from {filename}....')
    with open('scrape/' + filename) as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
    output_list = []
    for link in soup.find_all('a'):
        if 'reynoldsnlp.com/scrape' in link['href']:
            output_list.append(link['href'].split('/')[-1])
    return output_list
    # The preceding for loop could be replaced with this comprehension...
    # return [link['href'].split('/')[-1]
    #         for link in soup.find_all('a')
    #         if 'reynoldsnlp.com/scrape' in link['href']]


todo = {'aa.html'}  # seed filename
done = set()  # filenames that have already been requested
while todo:
    fname = todo.pop()
    get_reynoldsnlp(fname)
    new_hrefs = get_hrefs(fname)
    for new_href in new_hrefs:
        if new_href not in done:
            todo.add(new_href)
    # The preceding for loop could be replaced with this comprehension...
    # todo.update({h for h in new_hrefs if h not in done})
    done.add(fname)

names = sorted(u.split('/')[-1][:2] for u in glob('scrape/*.html'))
print(len(names), names)

# 1. We are missing fa.html
# 2. Sets are better because they cannot contain duplicates
