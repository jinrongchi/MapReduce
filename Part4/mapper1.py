#!/usr/bin/env python
"""mapper.py"""

import sys
import glob

files = glob.glob('inputDirectory/*', recursive = True)

for file in files:
    num = sum(len(line.split()) for line in open(file))
    with open(file) as f:
        lines = f.readlines()

        for line in lines:
            # remove leading and trailing whitespace
            line = line.strip()
            # split the line into words
            words = line.split()

	    # increase counters
            for word in words:

                term = file + ',' + word
                print('%s\t%s' % (term,1.0/num))

	# close the file at the end
        f.close()
