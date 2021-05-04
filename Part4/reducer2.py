#!/usr/bin/env python
"""reducer.py"""
from operator import itemgetter
import sys
import math

current_word = None
file_list = []
word = None
inputParameters = 3.0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    word, filename = line.split('\t', 1)
    if current_word == word:
        if(filename not in file_list):
            file_list.append(filename)
    else:
        if current_word:
            # write result to STDOUT
            for file_name in file_list:
                print('%s\tidf:%s' % (file_name + ',' + current_word, math.log10(inputParameters/len(file_list))))
        file_list = []
        file_list.append(filename)
        current_word = word
# do not forget to output the last word if needed!
if current_word == word:
    for file_name in file_list:
        print('%s\tidf:%s' % (file_name + ',' + current_word, math.log10(inputParameters/len(file_list))))
