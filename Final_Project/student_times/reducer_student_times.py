#!/usr/bin/python
import sys
import csv

from datetime import datetime

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    
    currentAuthor = None
    authorActivityFrequency = {}

    for line in reader:
        authorId = line[0]
        hour = line[1]
        
        if currentAuthor and currentAuthor != authorId and len(authorActivityFrequency) > 0:
            listOfMostFrequentHours = getKeysForBiggestAmount(authorActivityFrequency)
            writeOutput(currentAuthor, listOfMostFrequentHours)

            authorActivityFrequency = {}
        
        currentAuthor = authorId
        
        if hour not in authorActivityFrequency:
            authorActivityFrequency[hour] = 1
        elif hour in authorActivityFrequency:
            authorActivityFrequency[hour] += 1
    
    listOfMostFrequentHours = getKeysForBiggestAmount(authorActivityFrequency)
    writeOutput(currentAuthor, listOfMostFrequentHours) 

def getKeysForBiggestAmount(authorActivityFrequency):
    mostFrequent = 0
    listOfMostFrequentHours = None
    
    for hour in authorActivityFrequency:
        count = authorActivityFrequency[hour]
        
        if count > mostFrequent:
            mostFrequent = count
            listOfMostActiveHours = None
            listOfMostActiveHours = [hour]
        elif count == mostFrequent:
            listOfMostActiveHours.append(hour)

    return listOfMostActiveHours

def writeOutput(authorId, mostFrequentHours):
    writer = csv.writer(sys.stdout, delimiter='\t')
    
    for hour in mostFrequentHours:
        writer.writerow([authorId, hour])

def main():
    reducer()

if __name__ == "__main__":
    main()
