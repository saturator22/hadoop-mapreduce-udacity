#!/usr/bin/python

import sys

numberOfOccurences = 0
expectedString = "10.99.99.186"

for line in sys.stdin:
    
    if expectedString == line.strip():
        numberOfOccurences += 1

print "Total Occurences::", numberOfOccurences

