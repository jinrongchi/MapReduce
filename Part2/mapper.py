#!/usr/bin/env python
"""mapper.py"""
import sys

word_list = []

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    word_list.extend(words)

bigrams = [word_list[x:x+2] for x in range(len(word_list))]
# increase counters
for bigram in bigrams:
    # write the results to STDOUT (standard output); what we output here will be the input for the Reduce step, i.e. the
    # input for reducer.py
    #
    # tab-delimited; the trivial word count is 1
    if(len(bigram) == 2):
        bigram = bigram[0] + ' ' + bigram[1]
        print ('%s\t%s' % (bigram,1))
