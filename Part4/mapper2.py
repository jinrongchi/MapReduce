#!/usr/bin/env python
"""mapper.py"""

import sys
import glob

files = glob.glob('inputDirectory/*')
for file in files:

    with open(file) as f:

        lines = f.readlines()
        for line in lines:
            # remove leading and trailing whitespace
            line = line.strip()
            # split the line into words
            words = line.split()
            # increase counters
            for word in words:
                #term = word + ',' + file.split('/')[-1]
                print('%s\t%s' % (word, file.split('/')[-1]))
        # close the file at the end
        f.close()
