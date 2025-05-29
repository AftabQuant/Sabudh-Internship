import requests
from bs4 import BeautifulSoup

# Send a GET request to the Wikipedia main page
url = "https://en.wikipedia.org/wiki/Main_Page"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all header tags (h1 to h6)
header_tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# Display each header tag
for tag in header_tags:
    print(tag.string)
