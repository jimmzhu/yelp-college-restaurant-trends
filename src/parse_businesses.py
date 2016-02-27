import json
import os
from peak_check_in import find_peak_ci
from categories_histogram import *

DATA_DIR = os.path.dirname(os.path.abspath(__file__)) + '/../data/'
cities = ('Madison')

def process_businesses_json(json_path, process_fn=None):
    """ returns list of businesses given json file containing json businesses
    """
    results = []
    with open(DATA_DIR+json_path) as infile:
        for line in infile:
            if process_fn:
                process_fn(json.loads(line))
            else:
                results.push(json.loads(lin))
    return results

def businesses_to_csv(business, csv_path='training.csv', write_mode='a'):
    """ takes list of business (dicts) and outputs csv file """
    with open(DATA_DIR+csv_path, write_mode) as outfile:
        business_row = business_to_row(business)
        outfile.write(business_row.join(', ') + '\n')

def business_to_row(business):
    return [
        find_peak_ci(business)
    ]


def main():
    for city in cities:
        json_path = 'cities/%s/businesses.json' % city
        process_business_json(json_path, businesses_to_csv)

if __name__ == '__main__':
    main()
