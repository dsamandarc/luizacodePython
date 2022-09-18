import time 
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='geopyExercises')

def get_data(x):
    index, row = x     #selecting my row by index and by the content 
    time.sleep ( 1 )     #putting time between API acquisitions to avoid timeout
    

    response = geolocator.reverse(row['query'])


    place_id = response.raw['place_id'] if 'place_id' in response.raw else 'NA'
    osm_type = response.raw['osm_type'] if 'osm_type' in response.raw else 'NA'
    country = response.raw['address']['country'] if 'country' in response.raw else 'NA'
    country_code = response.raw['address']['country_code'] if 'country_code' in response.raw else 'NA'
        
    return place_id, osm_type, country, country_code