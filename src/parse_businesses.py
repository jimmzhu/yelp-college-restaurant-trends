import json
from constants import *
from peak_checkin import peak_checkins
from find_min_dist import find_min_dist_business, load_all_lat_long_data
from vectorize_categories import vectorize_categories, load_categories

ALL_CATEGORIES = load_categories()
LAT_LONG_DATA = load_all_lat_long_data()

def main():
    businesses_to_csv(aggregate_businesses_json(TRAIN_JSON), TRAIN_CSV)
    businesses_to_csv(aggregate_businesses_json(TEST_JSON), TEST_CSV)

def aggregate_businesses_json(json_path, function=lambda x,y: x+(y,), initial=()):
    """returns list of businesses given json file containing json businesses"""
    with open(json_path) as infile:
        for line in infile:
            initial = function(initial, json.loads(line))
    print 'JSON file loaded: %s' % json_path
    return initial

def businesses_to_csv(businesses, csv_path):
    """takes list of business (dicts) and outputs csv file"""
    with open(csv_path, 'w') as outfile:
        for i, business in enumerate(businesses):
            if (i+1) % 500 == 0:
                print '...%d' % (i+1)
            business_row = business_to_row(business)
            outfile.write(', '.join(business_row) + '\n')

def business_to_row(business):
    return reduce(str_flatten, (
        peak_checkins(business),                         # 1x56 (8 bins per day)
        vectorize_categories(business, ALL_CATEGORIES),  # 1x168
        find_min_dist_business(business, LAT_LONG_DATA), # 1x1
    ), ())

def str_flatten(current, other):
    if hasattr(other, '__iter__'):
        return current + tuple(map(str, other))
    return current + (str(other),)

if __name__ == '__main__':
    main()
