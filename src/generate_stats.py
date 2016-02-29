from constants import *
from parse_businesses import aggregate_businesses_json

def all_checkins(json_path=TRAIN_JSON):
    return aggregate_businesses_json(json_path, merge_checkins, {})

def merge_checkins(b1, b2, key='checkin_info'):
    return merge_histograms((b1.get(key) or {}), (b2.get(key) or {}))

def merge_histograms(h1, h2):
    return { k: h1.get(k,0) + h2.get(k,0) for k in set(h1.keys() + h2.keys()) }
