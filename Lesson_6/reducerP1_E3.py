#!/usr/bin/python

import sys

numberOfSales = 0
totalSale = 0

for line in sys.stdin:

    totalSale += float(line)
    numberOfSales += 1

print "Total Sale::", totalSale, "numberOfSales::", numberOfSales

