#!/usr/bin/python

import sys

oldKey = None
highestIndividualSale = 0

for line in sys.stdin:
    
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey = data_mapped[0]
    thisSale = float(data_mapped[1])

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", highestIndividualSale
        oldKey = thisKey
        highestIndividualSale = 0

    oldKey = thisKey
    if thisSale > highestIndividualSale:
        highestIndividualSale = thisSale

if oldKey:
    print oldKey, "\t", highestIndividualSale

