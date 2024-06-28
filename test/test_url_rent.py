import cloudscraper
from bs4 import BeautifulSoup

# Initialize the scraper
scraper = cloudscraper.create_scraper()

root_url2 = "https://www.immoweb.be/en/search/house/for-rent?countries=BE&page="
page2 = 95

while True:
    html2 = scraper.get(f"{root_url2}{page2}")
    status2 = html2.status_code
    print(f"Checking page: {page2}, Status code: {status2}")

    soup = BeautifulSoup(html2.text, 'html.parser')

    # Find the error message element
    error_message_element = soup.find('h1', class_='title--1 page-error__title empty-state__title')

    if error_message_element:
        error_message_text = error_message_element.text.strip()
        print(f"Found error message: {error_message_text}")

        if "Sorry, no matching results." in error_message_text:
            print("No more matching results found. Exiting loop.")
            break

    # Increment the page number for the next iteration
    page2 += 1
