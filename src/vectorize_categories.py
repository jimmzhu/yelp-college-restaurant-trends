#This script will transform a business's categories into a vector with the 1-Hot encoding.
# (If a category exists for a business, then we will place a 1 in the corresponding slot in )

from constants import *
import json

CATEGORIES_ATTRIBUTE = 'categories'

def load_categories():
    with open(DATA_DIR + 'categories.json') as f:
        categories_list = json.load(f)

    return categories_list

def vectorize_categories(business, categories_list):
    total_categories = len(categories_list)

    #Initially create a 251 dimensional array. (Or however many unique categories there are.)
    result = [0] * total_categories

    #Place 1's in the positions that correspond to where the business's categories are.
    for elt in business[CATEGORIES_ATTRIBUTE]:

        #Ignore all categories not in training set.
        if elt in categories_list:
            result[categories_list.index( elt )] = 1

    return result;

def main():

    #Run a quick example
    b1 = json.loads('{"business_id": "5UmKMjUEUNdYWqANhGckJw", "full_address": "4734 Lebanon Church Rd Dravosburg, PA 15034", "hours": {"Friday": {"close": "21:00", "open": "11:00"}, "Tuesday": {"close": "21:00", "open": "11:00"}, "Thursday": {"close": "21:00", "open": "11:00"}, "Wednesday": {"close": "21:00", "open": "11:00"}, "Monday": {"close": "21:00", "open": "11:00"}}, "open": true, "categories": ["Fast Food", "Restaurants"], "city": "Dravosburg", "review_count": 4, "name": "Mr Hoagie", "neighborhoods": [], "longitude": -79.9007057, "state": "PA", "stars": 4.5, "latitude": 40.3543266, "attributes": {"Take-out": true, "Drive-Thru": false, "Good For": {"dessert": false, "latenight": false, "lunch": false, "dinner": false, "brunch": false, "breakfast": false}, "Caters": false, "Noise Level": "average", "Takes Reservations": false, "Delivery": false, "Ambience": {"romantic": false, "intimate": false, "classy": false, "hipster": false, "divey": false, "touristy": false, "trendy": false, "upscale": false, "casual": false}, "Parking": {"garage": false, "street": false, "validated": false, "lot": false, "valet": false}, "Has TV": false, "Outdoor Seating": false, "Attire": "casual", "Alcohol": "none", "Waiter Service": false, "Accepts Credit Cards": true, "Good for Kids": true, "Good For Groups": true, "Price Range": 1}, "type": "business"}')

    print vectorize_categories( b1 )

if __name__ == '__main__':
    main()
