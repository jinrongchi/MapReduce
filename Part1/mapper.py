#!/usr/bin/env python
"""mapper.py"""

import sys
import os

# the path that stores list of document
path = "inputDirectory/"

# get file from the path
for doc_id in os.listdir(path):

    with open(path + doc_id) as f:
        lines = f.readlines()

        for line in lines:
            # remove leading and trailing whitespace
            line = line.strip()
            # split the line into words
            words = line.split()

	    # increase counters
            for word in words:

                term = word + ',' + doc_id
                print('%s\t%s' % (term,1))

	# close the file at the end
        f.close()
