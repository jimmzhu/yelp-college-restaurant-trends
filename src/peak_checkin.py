import json
from utils import *
from math import pi, cos, sin
from numpy import array

CHECKIN_INFO_ATTRIBUTE = 'checkin_info'
DAYS_PER_WEEK = 7
HOURS_PER_DAY = 24
CHECKIN_BINS_PER_DAY = (
    (0,7), (7,11), (9,13), (11,15), (13,17), (17,20), (19,21), (21,24)
)

def peak_checkins(business):
    """input is a dict representing a business object"""
    checkin_info = business[CHECKIN_INFO_ATTRIBUTE]
    checkins = [0.0] * DAYS_PER_WEEK * HOURS_PER_DAY
    if checkin_info is None:
        return (0.0,) * len(CHECKIN_BINS_PER_DAY) * DAYS_PER_WEEK

    for checkin_time, count in checkin_info.iteritems():
        hour, day = checkin_time.split('-')
        checkins[int(day)*HOURS_PER_DAY + int(hour)] += count

    checkins = array(checkins) / sum(checkins)
    binned_checkins = [0.0] * len(CHECKIN_BINS_PER_DAY) * DAYS_PER_WEEK
    for day in xrange(DAYS_PER_WEEK):
        for i, bin_range in enumerate(CHECKIN_BINS_PER_DAY):
            bin_start, bin_end = bin_range
            bin_start += day * HOURS_PER_DAY
            bin_end += day * HOURS_PER_DAY
            binned_checkins[day*len(CHECKIN_BINS_PER_DAY) + i] = \
                sum(checkins[bin_start:bin_end])

    return tuple(binned_checkins)

#    if checkin_info is None:
#        return (0,) * limit * 4
#
#    peak_checkins = \
#        sorted(checkin_info.items(), key=lambda x: x[1], reverse=True)[:limit]
#    return flat_map(vectorize_checkin_count, peak_checkins)

def vectorize_checkin_count(checkin_count):
    checkin_time, count = checkin_count
    hour, day = checkin_time.split('-')
    hour_angle = 2*pi * int(hour-1) / HOURS_PER_DAY
    day_angle = 2*pi * int(day) / DAYS_PER_WEEK
    return (cos(day_angle), sin(day_angle), cos(hour_angle), sin(hour_angle))
