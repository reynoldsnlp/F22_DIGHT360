"""Scrape and "parse" an HTML file."""

import re

import requests

url = 'https://www.reddit.com/r/Python/'  # TODO change me
header = {'user-agent': 'Rob Reynolds (robert_reynolds@byu.edu)'}  # TODO changeme
http_response = requests.get(url, headers=header)
src = http_response.text

print(src)

# TODO save HTML to a file (you may want to copy-paste this file to regex101.com to work on your regular expression(s)
# TODO Use regular expressions to extract useful information
# TODO Write the extracted data to a file
