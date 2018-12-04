#!/usr/bin/python

import sys

def reducer():

    currentDay = None
    totalSale = 0

    for line in sys.stdin:
        mappedData = line.strip().split("\t")
        
        weekday = mappedData[0]
        cost = float(mappedData[1])
        
        if currentDay and currentDay != weekday:
            print currentDay, ":::TOTAL SALE:::", totalSale
            totalSale = 0

        currentDay = weekday
        totalSale += cost
        
    print currentDay, ":::TOTAL SALE:::", totalSale

def main():
    reducer()

if __name__ == "__main__":
    main()
