import json
from constants import *
from peak_checkin import peak_checkins
from find_min_dist import find_min_dist_business

def main():
    businesses_to_csv(aggregate_businesses_json(TRAIN_JSON), TRAIN_CSV)
    businesses_to_csv(aggregate_businesses_json(TEST_JSON), TEST_CSV)

def aggregate_businesses_json(json_path, function=lambda x,y: x+(y,), initial=()):
    """returns list of businesses given json file containing json businesses"""
    with open(json_path) as infile:
        for i, line in enumerate(infile):
            if (i+1) % 500 == 0:
                print '...%d' % (i+1)
            initial = function(initial, json.loads(line))
    return initial

def businesses_to_csv(businesses, csv_path):
    """takes list of business (dicts) and outputs csv file"""
    with open(csv_path, 'w') as outfile:
        for business in businesses:
            business_row = business_to_row(business)
            outfile.write(', '.join(business_row) + '\n')

def business_to_row(business):
    return reduce(str_flatten, (
        peak_checkins(business, 3),  # 1x9 (top 3 checkins: (day, hour, count))
        find_min_dist_business(business),     # 1x1
    ), ())

def str_flatten(current, other):
    if hasattr(other, '__iter__'):
        return current + tuple(map(str, other))
    return current + (str(other),)

if __name__ == '__main__':
    main()
