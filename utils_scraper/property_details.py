import json
from selectolax.parser import HTMLParser
import chompjs
import cloudscraper

class ImmowebFeatures:
    """
    A class to scrape detailed property information from a given Immoweb property URL.

    Attributes
    ----------
    scraper : cloudscraper.CloudScraper
        The scraper object to handle requests.
    url : str
        The URL of the property to scrape.
    """
    def __init__(self, url):
        self.scraper = cloudscraper.create_scraper()
        self.url = url

    def scrape_features(self):
        """
        Initializes the ImmowebFeatures with a specific URL.

        Parameters
        ----------
        url : str
            The URL of the property to scrape.
        """
        try:
            response = self.scraper.get(self.url)
            if response.status_code != 200:
                print(f"Failed to retrieve {self.url}: Status code {response.status_code}")
                return None
            html = HTMLParser(response.text)
            html_data = html.css("script[type='text/javascript']")
            for script in html_data:
                try:
                    data = chompjs.parse_js_object(script.text())
                    return data
                except:
                    continue
            print(f"No valid data found in {self.url}")
            return None
        except Exception as e:
            print(f"An error occurred while scraping {self.url}: {e}")
            return None
