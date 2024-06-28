from selectolax.parser import HTMLParser
import chompjs
import cloudscraper
import pandas as pd


scraper = cloudscraper.create_scraper()


urls = [
    "https://www.immoweb.be/en/classified/house/for-sale/nassogne/6950/11485698","https://www.immoweb.be/en/classified/house/for-sale/borgerhout/2140/20001659"]




def web_info(url):
    resp = scraper.get(url)
    html = HTMLParser(resp.text)
    html_data = html.css("script[type='text/javascript']")
    
    data = {}

    for script in html_data:
        try:
            js_object = chompjs.parse_js_object(script.text())
            if 'price' in js_object and 'mainValue' in js_object['price']:
                data['price'] = js_object['price']['mainValue']
            if 'property' in js_object:
                property_info = js_object['property']
                if 'building' in property_info and 'condition' in property_info['building']:
                    data['building_condition'] = property_info['building']['condition']
                if 'land' in property_info and 'surface' in property_info['land']:
                    data['surface_of_the_plot'] = property_info['land']['surface']
                if 'building' in property_info and 'facadeCount' in property_info['building']:
                    data['number_of_facades'] = property_info['building']['facadeCount']
                if 'netHabitableSurface' in property_info:
                    data['living_area'] = property_info['netHabitableSurface']
                if 'location' in property_info and 'locality' in property_info['location']:
                    data['address'] = property_info['location']['locality']
                if 'type' in property_info:
                    data['property_type'] = property_info['type']
                if 'bedroomCount' in property_info:
                    data['bedroom'] = property_info['bedroomCount']
                if 'area' in property_info:
                    data['living_area'] = property_info['area']
                if 'hasTerrace' in property_info:
                    data['terrace'] = property_info['hasTerrace']
                    if property_info['hasTerrace'] and 'terraceSurface' in property_info:
                        data['terrace_area'] = property_info['terraceSurface']
                if 'kitchen' in property_info:
                    data['kitchen'] = "Yes" if property_info['kitchen'] else "No"
                if 'fireplaceCount' in property_info:
                    data['fireplace'] = "Yes" if property_info['fireplaceCount'] else "No"
                if 'hasSwimmingPool' in property_info:
                    data['swimmingPool'] = "Yes" if property_info['hasSwimmingPool'] else "No"
                if 'hasGarden' in property_info:
                    data['garden'] = "Yes" if property_info['hasGarden'] else "No"
                    if property_info['hasGarden'] and 'gardenSurface' in property_info:
                        data['garden_area'] = property_info['gardenSurface']
        except:
            pass

    return data


data = []

for url in urls:
    houses = web_info(url)
    data.append(houses)

df = pd.DataFrame(data)
print(df)