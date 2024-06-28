# File to obtain the data of one page inside data variable in scaper_onepgage.py

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

