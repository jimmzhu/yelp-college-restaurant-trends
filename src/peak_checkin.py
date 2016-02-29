import json
from utils import *

CHECKIN_INFO_ATTRIBUTE = 'checkin_info'

def peak_checkins(business, limit=3):
    """input is a dict representing a business object"""
    checkin_info = business[CHECKIN_INFO_ATTRIBUTE]
    if checkin_info is None:
        return (-1,) * limit * 3

    peak_checkins = \
        sorted(checkin_info.items(), key=lambda x: x[1], reverse=True)[:limit]
    return flat_map(vectorize_checkin_count, peak_checkins)

def vectorize_checkin_count(checkin_count):
    checkin_time, count = checkin_count
    hour, day = checkin_time.split('-')
    return (int(day), int(hour), count)
