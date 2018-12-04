#!/usr/bin/python

import sys

weekdayTransactions = {}
def reducer():
    for line in sys.stdin:
        mappedData = line.split("\t")
        
        weekday = mappedData[0].strip()
        cost = float(mappedData[1].strip())

        if weekday not in weekdayTransactions:
    	    numberOfTransactions = 1
            weekdayTransactions[weekday] = [cost, numberOfTransactions]
        else:
            weekdayTransactions[weekday][0] += cost
    	    weekdayTransactions[weekday][1] += 1

    for weekday in weekdayTransactions:
        mean = weekdayTransactions[weekday][0]/weekdayTransactions[weekday][1]
        print weekday , ":::Mean:::", mean    

def main():
    reducer()

if __name__ == "__main__":
    main()
