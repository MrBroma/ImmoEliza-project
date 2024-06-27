from selectolax.parser import HTMLParser
import chompjs
import cloudscraper
import json

# Initialize the scraper
scraper = cloudscraper.create_scraper()

url = "https://www.immoweb.be/en/classified/house/for-sale/nassogne/6950/11485698"

resp = scraper.get(f"{url}")
html = HTMLParser(resp.text)

html_data = html.css("script[type='text/javascript']")

for script in html_data:
    try:
        data = chompjs.parse_js_object(script.text())
        print(data)
    except:
        pass


