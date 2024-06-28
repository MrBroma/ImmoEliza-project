import cloudscraper
from bs4 import BeautifulSoup
import json

# Initialize the scraper
scraper = cloudscraper.create_scraper()

# Root URL of Immoweb website to use and URL suffix
root_url = "https://www.immoweb.be/en/search/house/for-sale?countries=BE&page="

page = 333
status = 200
url_dict = []
url_count = 1

while status == 200:
    html = scraper.get(f"{root_url}{page}")
    status = html.status_code
    print(page, status)

    soup = BeautifulSoup(html.text, 'html.parser')

    for h2 in soup.find_all('h2', class_='card__title card--result__title'):
        for link in h2.find_all('a', class_='card__title-link'):
            url = link.get('href')
            url_dict.append(url)
            url_count += 1
    page += 1

# Write the collected URLs to a JSON file
with open('links.json', 'w') as json_file:
    json.dump(url_dict, json_file, indent=4)

