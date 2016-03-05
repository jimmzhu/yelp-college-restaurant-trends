#!/usr/bin/env python

import os
import psycopg2

schema_file = os.path.dirname(os.path.abspath(__file__)) + '/schema.sql'
conn = psycopg2.connect('postgres:///yelp_learning')
cursor = conn.cursor()

cursor.execute(open(schema_file, 'r').read())

conn.commit()
cursor.close()
conn.close()
