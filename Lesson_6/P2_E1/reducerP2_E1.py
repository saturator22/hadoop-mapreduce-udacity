#!/usr/bin/python

import sys

numberOfOccurences = 0
expectedString = "/assets/js/the-associates.js"

for line in sys.stdin:
    
    if expectedString in line:
        numberOfOccurences += 1

print "Total Occurences::", numberOfOccurences

