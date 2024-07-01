# script to export URLs from the immoweb webstire
import cloudscraper
from bs4 import BeautifulSoup
import json

class ImmowebScraper:
    """
    A class to scrape property URLs from Immoweb.

    Attributes
    ----------
    root_url : str
        The root URL of the Immoweb search page.
    suffix_url : str
        The suffix to append to the root URL for pagination and ordering.
    scraper : cloudscraper.CloudScraper
        The scraper object to handle requests.
    url_dict : dict
        A dictionary to store the scraped URLs.
    url_count : int
        A counter to keep track of the number of URLs scraped.
    """
    def __init__(self, status_code: int = 200)-> None:
        """
        Initializes the ImmowebScraper with default values.
        """
        self.scraper = cloudscraper.create_scraper()
        self.root_url = "https://www.immoweb.be/en/search/house/for-sale?countries=BE&page="
        self.status_code = status_code
        self.url_list = []

    def scrape_urls(self) -> None:
        """
        Scrapes property URLs from Immoweb and stores them in url_dict.
        """
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

    def save_urls_to_json(self, filename: str ='links.json') -> None:
        with open(filename, 'w') as json_file:
            json.dump(self.url_list, json_file, indent=4)

obj = ImmowebScraper(200)

obj.scrape_urls()
obj.save_urls_to_json()

