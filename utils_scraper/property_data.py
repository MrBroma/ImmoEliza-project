import requests
from selectolax.parser import HTMLParser
import chompjs
import cloudscraper
import json

class Property_data:

    def __init__(self, data_dict):
        self.data_dict = data_dict
        pass

    def property_id(self):
        return self.data_dict['id']

    def locality(self):
        if (self.data_dict.get('property') and self.data_dict['property'].get('location') and 'locality' in self.data_dict['property']['location']):
            return self.data_dict['property']['location']['locality']
        return None

    def property_type(self):
        if (self.data_dict.get('property') and 'type' in self.data_dict['property']):
            return self.data_dict['property']['type']
        return None

    def property_subtype(self):
        if (self.data_dict.get('property') and 'subtype' in self.data_dict['property']):
            return self.data_dict['property']['subtype']
        return None

    def price(self):
        if (self.data_dict.get('transaction') and self.data_dict['transaction'].get('sale') and 'price' in self.data_dict['transaction']['sale']):
            return self.data_dict['transaction']['sale']['price']
        return None
    
    def sale_type(self):
        if (self.data_dict.get('price') and 'type' in self.data_dict['price']):
            return self.data_dict['price']['type']
        return None

    def room_number(self):
        if (self.data_dict.get('property') and 'bedroomCount' in self.data_dict['property']):
            return self.data_dict['property']['bedroomCount']
        return None

    def bathroom_number(self):
        if (self.data_dict.get('property') and 'bathroomCount' in self.data_dict['property']):
            return self.data_dict['property']['bathroomCount']
        return None

    def living_area(self):
        if (self.data_dict.get('property') and 'netHabitableSurface' in self.data_dict['property']):
            return self.data_dict['property']['netHabitableSurface']
        return None
    
    def kitchen(self):
        if (self.data_dict.get('property') and self.data_dict['property'].get('kitchen') and 'type' in self.data_dict['property']['kitchen']):
            return self.data_dict['property']['kitchen']['type']
        return None

    def fireplace(self):
        if (self.data_dict.get('property') and 'fireplaceCount' in self.data_dict['property']):
            return self.data_dict['property']['fireplaceCount']
        return None

    def terrace(self):
        if (self.data_dict.get('property') and 'hasTerrace' in self.data_dict['property']):
            return self.data_dict['property']['hasTerrace']
        return None

    def terrace_surface(self):
        if (self.data_dict.get('property') and 'terraceSurface' in self.data_dict['property']):
            return self.data_dict['property']['terraceSurface']
        return None

    def garden(self):
        if (self.data_dict.get('property') and 'hasGarden' in self.data_dict['property']):
            return self.data_dict['property']['terraceSurface']
        return None
    
    def garden_surface(self):
        if (self.data_dict.get('property') and 'gardenSurface' in self.data_dict['property']):
            return self.data_dict['property']['gardenSurface']
        return None

    def plot_surface(self):
        if (self.data_dict.get('property') and self.data_dict['property'].get('land') and 'surface' in self.data_dict['property']['land']):
            return self.data_dict['property']['land']['surface']
        return None

    def facade_number(self):
        if (self.data_dict.get('property') and self.data_dict['property'].get('building') and 'facadeCount' in self.data_dict['property']['building']):
            return self.data_dict['property']['building']['facadeCount']
        return None
        
    def swimmingpool(self):
        if (self.data_dict.get('property') and 'hasSwimmingPool' in self.data_dict['property']):
            return self.data_dict['property']['hasSwimmingPool']
        return None

    def building_condition(self):
        if (self.data_dict.get('property') and self.data_dict['property'].get('building') and 'condition' in self.data_dict['property']['building']):
            return self.data_dict['property']['building']['condition']
        return None


# Initialize the scraper
scraper = cloudscraper.create_scraper()

url = "https://www.immoweb.be/en/classified/house/for-sale/erpe-mere/9420/11472054"

resp = scraper.get(f"{url}")
html = HTMLParser(resp.text)

html_data = html.css("script[type='text/javascript']")

for script in html_data:
    data_dict = chompjs.parse_js_object(script.text())
    break

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

