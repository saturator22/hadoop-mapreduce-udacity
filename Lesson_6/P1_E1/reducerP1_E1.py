#!/usr/bin/python

import sys

oldKey = None
combinedSale = 0

for line in sys.stdin:

    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    
    category = data_mapped[0]
    cost = float(data_mapped[1])
    
    if oldKey and oldKey != category:
        print oldKey, "\t", combinedSale
        oldKey = category
        combinedSale = 0
    
    oldKey = category
    combinedSale += cost

if oldKey:
    print oldKey, "\t", combinedSale

