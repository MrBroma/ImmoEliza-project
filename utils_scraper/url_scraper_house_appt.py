import cloudscraper
from bs4 import BeautifulSoup
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

class ImmowebScraper:
    def __init__(self, property_type: str, status_code: int = 200) -> None:
        self.scraper = cloudscraper.create_scraper()
        self.root_url = f"https://www.immoweb.be/en/search/{property_type}/for-sale?countries=BE&page="
        self.status_code = status_code
        self.url_list = []
        self.page_range = 20  # Number of pages to scrape in parallel

    def fetch_page(self, page: int):
        url = f"{self.root_url}{page}"
        html = self.scraper.get(url)
        return html.text if html.status_code == 200 else None

    def scrape_urls(self) -> None:
        page = 1
        while True:
            with ThreadPoolExecutor(max_workers=self.page_range) as executor:
                futures = {executor.submit(self.fetch_page, page + i): page + i for i in range(self.page_range)}
                results = []
                for future in as_completed(futures):
                    result = future.result()
                    if result:
                        results.append(result)
                    else:
                        self.status_code = 404
                        break
                
                if not results:
                    break

                for html in results:
                    soup = BeautifulSoup(html, 'html.parser')
                    for h2 in soup.find_all('h2', class_='card__title card--result__title'):
                        for link in h2.find_all('a', class_='card__title-link'):
                            url = link.get('href')
                            self.url_list.append(url)

            if self.status_code != 200:
                break

            page += self.page_range
            print(f"Completed pages up to {page-1}")

    @staticmethod
    def save_urls_to_json(url_list, filename: str = 'links.json') -> None:
        with open(filename, 'w') as json_file:
            json.dump(url_list, json_file, indent=4)

# Main function to scrape both houses and apartments
def main():
    combined_url_list = []

    # Scrape house URLs
    house_scraper = ImmowebScraper(property_type='house')
    house_scraper.scrape_urls()
    combined_url_list.extend(house_scraper.url_list)

    # Scrape apartment URLs
    apartment_scraper = ImmowebScraper(property_type='apartment')
    apartment_scraper.scrape_urls()
    combined_url_list.extend(apartment_scraper.url_list)

    # Save combined URLs to a single JSON file
    ImmowebScraper.save_urls_to_json(combined_url_list, 'combined_links.json')

if __name__ == "__main__":
    main()
