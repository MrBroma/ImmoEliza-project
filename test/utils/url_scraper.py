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


# root_url2 = "https://www.immoweb.be/en/search/house/for-rent?countries=BE&page="

# page2 = 95
# status = ""
# url_dict = []
# url_count2 = 1

# while True:
#     html2 = scraper.get(f"{root_url2}{page2}")
#     status2 = html2.status_code
#     print(page2)
#     soup = BeautifulSoup(html2.text, 'html.parser')

#     test = soup.find_all('h1', class_='title--1 page-error__title empty-state__title')
#     print(str(test))
    
#     for link2 in soup.find_all('h2', class_='card__title card--result__title'):
#             url2 = link2.get('href')
#             url_dict.append(url2)
#             url_count2 += 1
#     page2 += 1


# Write the collected URLs to a JSON file
with open('links.json', 'w') as json_file:
    json.dump(url_dict, json_file, indent=4)




# def extract_urls(page_number):
#     url = f"https://www.immoweb.be/en/search/house/for-sale?countries=BE&page={page_number}"
#     page = scraper.get(url)
#     soup = BeautifulSoup(page.text, "html.parser")

#     for link in soup.find_all('a', href=True):
#         href = link['href']
#         if '/en/classified/house/for-sale' in href:  
#             full_url = f"https://www.immoweb.be{href}"
#             data_url.append(full_url)
    
# while current_page <= max_pages:
#     extract_urls(current_page)
#     current_page += 1
