import csv
from constants import *
from math import *

path_to_latlongdata = DATA_DIR + 'college_lat_long.csv'
LAT_LONG_DATA = None

def find_min_dist_business(business):
    return find_min_dist(business['latitude'], business['longitude'])

def load_all_lat_long_data():
    #Function retrieves all of the Longitude Latitude pairs coming from the CSV
    #file mentioned above.
    print 'load_all_lat_long_data called'

    with open(path_to_latlongdata,'rb') as csvfile:
        loc_reader = csv.reader(csvfile, delimiter=',')

        lat_long_array = []

        for i, line in enumerate(loc_reader):
            if i == 0:
                continue

            #array = line.split(',')
            #print line
#            print i , 'lat: ' + line[4] , 'long: ' + line[3]


            elt = {}
            elt['latitude']  = float( line[4] )
            elt['longitude'] = float( line[3] )

            lat_long_array.append( elt )

#    print 'Created array of latitude-longitude pairs.'

    return lat_long_array

def find_min_dist( business_latitude , business_longitude ):
    global LAT_LONG_DATA

    if LAT_LONG_DATA is None:
        LAT_LONG_DATA = load_all_lat_long_data()

    ll_array = LAT_LONG_DATA

    #Create an array of dictionaries, where each dictionary contains:
    # - Latitude Coordinate (saved under the 'latitude' bin)
    # - Longitude Coordinate (saved under the 'longitude' bin)

    ll_array = load_all_lat_long_data()

    #Find minimum distance between a given business JSON object and ALL of the pairs in this list
    distances = []

    for location in ll_array:

        distances.append( sqrt( pow(location['latitude'] - business_latitude , 2) + pow( location['longitude'] - business_longitude , 2 ) ) )

#    print distances

#    print 'Minimum is: ',str(min(distances))

    return min(distances)


def main():

    #Input JSON Object with latitude longitude coordinates inside
    #     b1 = '{"business_id": "5UmKMjUEUNdYWqANhGckJw", "full_address": "4734 Lebanon Church Rd\nDravosburg, PA 15034", "hours": {"Friday": {"close": "21:00", "open": "11:00"}, "Tuesday": {"close": "21:00", "open": "11:00"}, "Thursday": {"close": "21:00", "open": "11:00"}, "Wednesday": {"close": "21:00", "open": "11:00"}, "Monday": {"close": "21:00", "open": "11:00"}}, "open": true, "categories": ["Fast Food", "Restaurants"], "city": "Dravosburg", "review_count": 4, "name": "Mr Hoagie", "neighborhoods": [], "longitude": -79.9007057, "state": "PA", "stars": 4.5, "latitude": 40.3543266, "attributes": {"Take-out": true, "Drive-Thru": false, "Good For": {"dessert": false, "latenight": false, "lunch": false, "dinner": false, "brunch": false, "breakfast": false}, "Caters": false, "Noise Level": "average", "Takes Reservations": false, "Delivery": false, "Ambience": {"romantic": false, "intimate": false, "classy": false, "hipster": false, "divey": false, "touristy": false, "trendy": false, "upscale": false, "casual": false}, "Parking": {"garage": false, "street": false, "validated": false, "lot": false, "valet": false}, "Has TV": false, "Outdoor Seating": false, "Attire": "casual", "Alcohol": "none", "Waiter Service": false, "Accepts Credit Cards": true, "Good for Kids": true, "Good For Groups": true, "Price Range": 1}, "type": "business"}'
    # Function should receive as input the values in the following entries of the dictionary: "latitude": 40.3543266, "longitude": -79.9007057
    ex_lat  = 40.3543266
    ex_long = -79.9007057

    find_min_dist( ex_lat , ex_long )


if __name__ == '__main__':
    main()
