#!/usr/bin/env python
import sqlalchemy
import os

schema_file = os.path.dirname(os.path.abspath(__file__)) + '/schema.sql'

engine = sqlalchemy.create_engine('postgres:///yelp_learning')
conn = engine.connect()
conn.execute(open(schema_file, 'r').read())
conn.close()
