import requests
from bs4 import BeautifulSoup

# Target URL
url = 'https://www.linkedin.com/feed/'  # Replace with the actual URL

# Send GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract specific data, for example, all links
    links = soup.find_all('a')

    # Print each link
    for link in links:
        print(link.get('href'))
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
