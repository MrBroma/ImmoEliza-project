import requests
from selectolax.parser import HTMLParser
import chompjs
import cloudscraper
import json
import pandas as pd
import Property_data from .utils_scraper/Property_data


classe = Property_data(data_dict)

# calling functions
house_id = classe.property_id()
city = classe.locality()
property_type = classe.property_type()
sub = classe.property_subtype()
price = classe.price()
sale_type = classe.sale_type()
rooms = classe.room_number()
bath = classe.bathroom_number()
area = classe.living_area()
kitchen = classe.kitchen()
fire = classe.fireplace()
terrace = classe.terrace()
terrace_m2 = classe.terrace_surface()
garden = classe.garden()
garden_m2 = classe.garden_surface()
surface = classe.plot_surface()
facade = classe.facade_number()
pool = classe.swimmingpool()
house_condition = classe.building_condition()


print(house_id, city, property_type, sub, price, sale_type, rooms, bath)
print(area, kitchen, fire, terrace, terrace_m2, garden, garden_m2, surface, facade)
print(pool, house_condition)

# Create a sample dataframe
property_dict = {'house_id' : [house_id],
                 'Locality' : [city],
                 'Property_type': [property_type],
                 'Property_subtype': [sub],
                 'Price' : [price]
                 }

df = pd.DataFrame(property_dict)

# Save the dataframe to a CSV file
df.to_csv('test_pro.csv', index=False)


