#!/usr/bin/python

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')

def mapper():
    for line in reader:
        nodeId = line[0]
        body = line[4]
        
        if not nodeId.isdigit():
            continue

        splittedBody = splitBody(body)
        
        for word in splittedBody:
            
            print nodeId, "\t", word

def splitBody(body):
    return re.split('[^a-zA-Z0-9]+', body)

def main():
    mapper()

if __name__ == "__main__":
    main()
