#!/usr/bin/env python

from datetime import date
from decimal import Decimal
import json
import os
import psycopg2
import psycopg2.extras

cities = ('Charlotte', 'Las Vegas', 'Madison', 'Phoenix',
          'Pittsburgh', 'Urbana-Champaign')

export_format = os.path.dirname(os.path.abspath(__file__)) + \
                '/../data/cities/%s/businesses.json'

sql_query = """
    SELECT businesses.business_id,
           min(businesses.name)                     AS name,
           min(businesses.neighborhoods)            AS neighborhoods,
           min(businesses.full_address)             AS full_address,
           min(businesses.city)                     AS city,
           min(businesses.state)                    AS state,
           min(businesses.latitude)                 AS latitude,
           min(businesses.longitude)                AS longitude,
           min(businesses.stars)                    AS stars,
           min(businesses.review_count)             AS review_count,
           min(businesses.categories)               AS categories,
           (array_agg(businesses.hours))[1]         AS hours,
           (array_agg(businesses.attributes))[1]    AS attributes,
           (array_agg(checkins.checkin_info))[1]    AS checkin_info,
           array_agg(reviews.stars)                 AS review_stars,
           array_agg(reviews.text)                  AS review_texts,
           array_agg(reviews.date)                  AS review_dates,
           array_agg(reviews.votes)                 AS review_votes
    FROM businesses
    INNER JOIN reviews ON reviews.business_id=businesses.business_id
    LEFT JOIN checkins ON checkins.business_id=businesses.business_id
    WHERE city = %s
      AND categories @> ('{Food}')
      AND open=true
    GROUP BY businesses.business_id;
"""

conn = psycopg2.connect('postgres:///yelp_learning')
cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

def main():
    for city in cities:
        print 'exporting Yelp data for ' + city + '...'
        export_table(city)
        conn.commit()
    cursor.close()
    conn.close()

def export_table(city):
    filename = export_format % city
    with open(filename, 'w') as outfile:
        cursor.execute(cursor.mogrify( sql_query, (city,) ))
        json_lines = (json.dumps(r, default=json_sanitize)+'\n' for r in cursor)
        outfile.writelines(json_lines)

def json_sanitize(value):
    if isinstance(value, Decimal):
        return float(value)
    if isinstance(value, date):
        return value.strftime('%Y-%m-%d')
    return value

if __name__ == '__main__':
    main()
