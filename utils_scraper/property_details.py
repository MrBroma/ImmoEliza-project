import json
from selectolax.parser import HTMLParser
import chompjs
import cloudscraper

class ImmowebFeatures:
    def __init__(self, url):
        self.scraper = cloudscraper.create_scraper()
        self.url = url

    def scrape_features(self):
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
