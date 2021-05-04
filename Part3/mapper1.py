#!/usr/bin/env python
"""mapper.py"""

import sys
import os

current_filename = ""
words_list = []

# input comes from STDIN (standard input)
for line in sys.stdin:
    # get the filename
    filename = os.environ["map_input_file"]
    filename = os.path.split(filename)[-1]

    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()

    if(current_filename == filename):
       words_list.extend(words)
    else:

        bigrams = [words_list[x:x+2] for x in range(len(words_list))]
        # increase counters
        for bigram in bigrams:
            if(len(bigram) == 2):
                bigram = bigram[0] + ' ' + bigram[1] + ',' + current_filename
                print ('%s\t%s' % (bigram,1))
        words_list = []
        words_list.extend(words)
        current_filename = filename

bigrams = [words_list[x:x+2] for x in range(len(words_list))]
# increase counters
for bigram in bigrams:
    if(len(bigram) == 2):
        bigram = bigram[0] + ' ' + bigram[1] + ',' + current_filename
        print ('%s\t%s' % (bigram,1))