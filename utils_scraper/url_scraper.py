# script to export URLs from the immoweb webstire
import cloudscraper
from bs4 import BeautifulSoup
import json

class ImmowebScraper:
    def __init__(self, status_code=200):
        self.scraper = cloudscraper.create_scraper()
        self.root_url = "https://www.immoweb.be/en/search/house/for-sale?countries=BE&page="
        self.status_code = status_code
        self.url_list = []

    def scrape_urls(self):
        page = 1
        while self.status_code == 200:
            url = f"{self.root_url}{page}"
            html = self.scraper.get(url)
            self.status_code = html.status_code

            soup = BeautifulSoup(html.text, 'html.parser')
            for h2 in soup.find_all('h2', class_='card__title card--result__title'):
                for link in h2.find_all('a', class_='card__title-link'):
                    url = link.get('href')
                    self.url_list.append(url)
            page += 1
            print(page, self.status_code)


    def save_urls_to_json(self, filename='links.json'):
        with open(filename, 'w') as json_file:
            json.dump(self.url_list, json_file, indent=4)

obj = ImmowebScraper(200)

obj.scrape_urls()
obj.save_urls_to_json()

