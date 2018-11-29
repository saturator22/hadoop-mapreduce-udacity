#!/usr/bin/python

import sys

currentPath = None
numberOfOccurences = 0

mostOccurences = 0
mostOccuredPath = None

for line in sys.stdin:
    
    line = line.strip()      
    
    if currentPath and currentPath != line:
        numberOfOccurences = 0
    
    currentPath = line
    numberOfOccurences += 1

    if numberOfOccurences > mostOccurences:
        mostOccurences = numberOfOccurences
        mostOccuredPath = currentPath
    
print "Most Occured Path::", mostOccuredPath, "Most Occurences::", mostOccurences

