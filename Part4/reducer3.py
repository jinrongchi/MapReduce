#!/usr/bin/env python
"""reducer.py"""
from operator import itemgetter
import sys

current_word = None
tf = 0.0
word = None

idf = 0.0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    word, tf = line.split('\t', 1)

    # convert count (currently a string) to float
    try:
        tf = float(tf.split(':')[1])
    except ValueError:
        # count was not a number, so silently ignore/discard this line
        continue

    if (current_word == word):
        print('((%s),\t%s\t%s\t%s)' % (current_word, tf, idf, idf*tf))
    else:
        current_word = word
        idf = tf