# File to obtain the data of one page inside data variable in scaper_onepage.py
class Property_data:
    """
    A class to hold and provide access to detailed property information.

    Attributes
    ----------
    data : dict
        The dictionary containing the property details.
    """

    def __init__(self, data):
        """
        Initializes the Property_data with a dictionary of property information.

        Parameters
        ----------
        data_dict : dict
            The dictionary containing the property details.
        """
        self.data = data
        pass

    def property_id(self):
        return self.data['id']

    def locality(self):
        if (self.data.get('property') and self.data['property'].get('location') and 'locality' in self.data['property']['location']):
            if self.data['property']['location']['locality'] == "":
                return None
            return self.data['property']['location']['locality']
        return None

    def property_type(self):
        if (self.data.get('property') and 'type' in self.data['property']):
            return self.data['property']['type']
        return None

    def property_subtype(self):
        if (self.data.get('property') and 'subtype' in self.data['property']):
            return self.data['property']['subtype']
        return None

    def price(self):
        if (self.data.get('transaction') and self.data['transaction'].get('sale') and 'price' in self.data['transaction']['sale']):
            return self.data['transaction']['sale']['price']
        return None
    
    def sale_type(self):
        if (self.data.get('price') and 'type' in self.data['price']):
            return self.data['price']['type']
        return None

    def room_number(self):
        if (self.data.get('property') and 'bedroomCount' in self.data['property']):
            return self.data['property']['bedroomCount']
        return None

    def bathroom_number(self):
        if (self.data.get('property') and 'bathroomCount' in self.data['property']):
            return self.data['property']['bathroomCount']
        return None

    def living_area(self):
        if (self.data.get('property') and 'netHabitableSurface' in self.data['property']):
            return self.data['property']['netHabitableSurface']
        return None
    
    def kitchen(self):
        if (self.data.get('property') and self.data['property'].get('kitchen') and 'type' in self.data['property']['kitchen']):
            return self.data['property']['kitchen']['type']
        return None

    def fireplace(self):
        if (self.data.get('property') and 'fireplaceExists' in self.data['property']):
            return self.data['property']['fireplaceExists']
        return None

    def terrace(self):
        if (self.data.get('property') and 'hasTerrace' in self.data['property']):
            return self.data['property']['hasTerrace']
        return None

    def terrace_surface(self):
        if (self.data.get('property') and 'terraceSurface' in self.data['property']):
            return self.data['property']['terraceSurface']
        return None

    def garden(self):
        if (self.data.get('property') and 'hasGarden' in self.data['property']):
            return self.data['property']['hasGarden']
        return None
    
    def garden_surface(self):
        if (self.data.get('property') and 'gardenSurface' in self.data['property']):
            return self.data['property']['gardenSurface']
        return None

    def plot_surface(self):
        if (self.data.get('property') and self.data['property'].get('land') and 'surface' in self.data['property']['land']):
            return self.data['property']['land']['surface']
        return None

    def facade_number(self):
        if (self.data.get('property') and self.data['property'].get('building') and 'facadeCount' in self.data['property']['building']):
            return self.data['property']['building']['facadeCount']
        return None
        
    def swimmingpool(self):
        if (self.data.get('property') and 'hasSwimmingPool' in self.data['property']):
            return self.data['property']['hasSwimmingPool']
        return None

    def building_condition(self):
        if (self.data.get('property') and self.data['property'].get('building') and 'condition' in self.data['property']['building']):
            return self.data['property']['building']['condition']
        return None

    def furnished(self):
        if (self.data.get('transaction') and self.data['transaction'].get('isFurnished') and 'price' in self.data['transaction']['sale']):
            return self.data['transaction']['sale']['isFurnished']
        return None
    
    def flood_zone(self):
        if (self.data.get('property') and self.data['property'].get('constructionPermit') and 'floodZoneType' in self.data['property']['constructionPermit']):
            return self.data['property']['constructionPermit']['floodZoneType']
        return None

