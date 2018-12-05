#!/usr/bin/python
import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')
    
    tagFrequency = {}
    
    for line in reader:
        nodeType = line[5]

        if not nodeType == "question":
            continue
	    
        tags = line[2].split()
        
        for tag in tags:
            if tag not in tagFrequency:
                tagFrequency[tag] = 1
            else:
                tagFrequency[tag] += 1

    for tag in tagFrequency:    	
        writer.writerow([tag, tagFrequency[tag]])

def main():
    mapper()

if __name__ == "__main__":
    main()
