#!\usr\bin\env python3
"""
  Take the first num_tweets tweets from a twitter data file and print each
  field on a seperate line and add a blank line between tweets.
"""
import csv

datfile = open('tweets.dat', 'w')
tsvfile = open('twitter_sm.tsv', 'r')
tsvreader = csv.reader(tsvfile, delimiter='\t')
num_tweets = 5

for i in range(num_tweets):
    line = tsvreader.__next__()
    for val in line:
        datfile.write(val + '\n')
    datfile.write('\n')
