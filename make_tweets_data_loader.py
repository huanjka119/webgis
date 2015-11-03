#!\usr\bin\env python3
"""
  Process data from a twitter data file and generate SQL INSERT statements to
  insert desired fields into a PostGIS database.
"""
import csv

sqlfile = open('load_tweets.sql', 'w')
insert_cmd = """INSERT INTO tweets VALUES (
  '{0}',
  ST_SetSRID(ST_MakePoint({1}, {2}), 4326),
  $slit${3}$slit$
);
"""

with open('twitter_sm.tsv') as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter='\t')
    for line in tsvreader:
        sqlfile.write(insert_cmd.format(line[0], line[5], line[6], line[-1]))

sqlfile.close()
