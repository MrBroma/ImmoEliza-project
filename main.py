import json
import os
import time
import pandas as pd
from utils_scraper.property_details import ImmowebFeatures
from utils_scraper.property_data import Property_data
from concurrent.futures import ThreadPoolExecutor, as_completed
from random import uniform

current_directory = os.path.dirname(__file__)
json_file_path = os.path.join(current_directory, 'links.json')

def scrape_and_save(link: str, csv_file_path: str) -> None:
    """
    Scrapes property details from a given URL and saves them to a CSV file.

    Parameters:
    - link (str): URL of the property to scrape.
    - csv_file_path (str): File path to save the property details CSV.

    Processes data through property detail classes and appends or creates a CSV
    file with property details. Handles missing data by replacing it with 'NaN'.
    """
    obj = ImmowebFeatures(link)
    data = obj.scrape_features()
    if data:
        property_obj = Property_data(data)
        property_dict = {
            "house_id": property_obj.property_id(),
            "city": property_obj.locality(),
            "property_type": property_obj.property_type(),
            "subtype": property_obj.property_subtype(),
            "price": property_obj.price(),
            "sale_type": property_obj.sale_type(),
            "rooms": property_obj.room_number(),
            "bathrooms": property_obj.bathroom_number(),
            "living_area": property_obj.living_area(),
            "kitchen": property_obj.kitchen(),
            "fireplace": property_obj.fireplace(),
            "terrace": property_obj.terrace(),
            "terrace_surface": property_obj.terrace_surface(),
            "garden": property_obj.garden(),
            "garden_surface": property_obj.garden_surface(),
            "plot_surface": property_obj.plot_surface(),
            "facade_number": property_obj.facade_number(),
            "swimming_pool": property_obj.swimmingpool(),
            "building_condition": property_obj.building_condition()
        }

        # Replace empty, None, or "null" values with NaN
        property_dict = {k: (v if v not in ["", None, "null"] else "NaN") for k, v in property_dict.items()}
        
        # Create a DataFrame for the current property
        df = pd.DataFrame([property_dict])
        
        # Save to CSV (append mode)
        if os.path.exists(csv_file_path):
            df.to_csv(csv_file_path, mode='a', header=False, index=False)
        else:
            df.to_csv(csv_file_path, mode='w', header=True, index=False)

def read_links(file_path: str, csv_file_path: str) -> None:
    """
    Reads property URLs from a JSON file and scrapes them in batches.

    Parameters:
    - file_path (str): Path to the JSON file containing property URLs.
    - csv_file_path (str): Path where the CSV file will be saved.

    Utilizes concurrent threads to speed up the scraping process and includes
    a random delay between batches to avoid hitting server-side rate limits.
    """
    with open(file_path, 'r') as url_immoweb:
        links = json.load(url_immoweb)

    batch_size = 20  # Number of concurrent threads to run
    total_links = len(links)
    
    with ThreadPoolExecutor(max_workers=batch_size) as executor:
        for i in range(0, total_links, batch_size):
            futures = [executor.submit(scrape_and_save, link, csv_file_path) for link in links[i:i + batch_size]]
            for future in as_completed(futures):
                future.result()
            time.sleep(uniform(2, 5))  # Random delay between batches

# File path for the CSV file
csv_file_path = os.path.join(current_directory, 'properties_data.csv')

# Run the scraping and save to CSV
read_links(json_file_path, csv_file_path)
