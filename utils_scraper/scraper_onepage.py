from selectolax.parser import HTMLParser
import chompjs
import cloudscraper

from property_data import Property_data


class ImmowebFeatures:
    def __init__(self, url):
        self.scraper = cloudscraper.create_scraper()
        self.url = url

    def scrape_features(self):
        response = self.scraper.get(self.url)
        html = HTMLParser(response.text)
        html_data = html.css("script[type='text/javascript']")

        for script in html_data:
            try:
                data = chompjs.parse_js_object(script.text())
                return data
            except:
                pass


with open(links., 'r') as json_file:
    json.dump(self.url_list, json_file, indent=4)

url = "https://www.immoweb.be/en/classified/house/for-sale/la-louviere/7100/11428289"

test = ImmowebFeatures(url)

print(test.scrape_features())


