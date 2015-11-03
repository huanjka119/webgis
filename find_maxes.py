#!\usr\bin\env python3
"""
  Find the maximum size (in characters) of each of the seperate fields in a
  set of Twitter data, store it in a list, and write it out to a file.
"""
import csv

maxes = 13 * [0]
f = open('maxes.dat', 'w')

with open('twitter_sm.tsv') as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter='\t')
    for line in tsvreader:
        for i, val in enumerate(line):
            if len(val) > maxes[i]:
                maxes[i] = len(val)

f.write(str(maxes))
f.close()
