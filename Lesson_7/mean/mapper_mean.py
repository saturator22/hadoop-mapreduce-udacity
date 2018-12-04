#!/usr/bin/python

import sys
from datetime import datetime

def mapper():
    numbersOfWeekdays = {
        0:"Monday",
        1:"Tuesday",
        2:"Wednesday",
        3:"Thursday",
        4:"Friday",
        5:"Saturday",
        6:"Sunday"    
    }    
        
    for line in sys.stdin:
        data = line.strip().split("\t")
    
        if len(data) == 6:
            date, time, store, item, cost, payment = data
        
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
    
        print numbersOfWeekdays[weekday], "\t", cost

def main():
    mapper()

if __name__ == "__main__":
    main()
