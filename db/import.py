#!/usr/bin/env python

import json
import os
import psycopg2
import unicodedata

data_dir = os.path.dirname(os.path.abspath(__file__)) + '/../data/raw/'
filenames = {
    'businesses': 'yelp_academic_dataset_business.json',
    'reviews':   'yelp_academic_dataset_review.json',
    'checkins':  'yelp_academic_dataset_checkin.json'
}
conn = psycopg2.connect('postgres:///yelp_learning')
cursor = conn.cursor()

def main():
    for table_name in ('businesses', 'reviews', 'checkins'):
        print 'importing ' + table_name + '...'
        import_table(table_name)
        conn.commit()
    cursor.close()
    conn.close()

def import_table(table_name, chunk_size=2000, max_rows=-1):
    filename = filenames[table_name]
    with open(data_dir + filename) as infile:
        chunk = []
        for i, line in enumerate(infile):
            chunk.append(json.loads(line))
            if i == max_rows:
                break

            if (i+1) % chunk_size == 0:
                import_rows(table_name, chunk)
                chunk = []
                if (i+1)/chunk_size % 10 == 0:
                    print '... ... %d records' % (i+1)

        import_rows(table_name, chunk)
        chunk = []

def import_rows(table_name, rows):
    if len(rows) == 0:
        return

    arg_format = '(' + ','.join(['%s']*len(rows[0])) + ')'

    insert_sql = 'INSERT INTO ' + table_name + ' '
    col_arg_sql = sanitize(arg_format % tuple(rows[0].keys()))
    row_arg_sqls = []
    for row in rows:
        values = (sanitize(v) for v in row.values())
        row_arg_sqls.append(cursor.mogrify(arg_format, tuple(values)))

    args_sql = col_arg_sql + ' VALUES ' + ','.join(row_arg_sqls)

    cursor.execute(insert_sql + args_sql)

def sanitize(value):
    if isinstance(value, dict):
        return json.dumps(value)
    if isinstance(value, unicode):
        return unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    return value

if __name__ == '__main__':
    main()
