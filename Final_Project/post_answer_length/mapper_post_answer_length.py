#!/usr/bin/python
import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')
    
    for line in reader:
        nodeType = line[5]

        if nodeType == "question":
            postId = line[0]
        elif nodeType == "answer":
            postId = line[6]
        else:
            continue        

    	bodyLength = len(line[4])
        writer.writerow([postId, nodeType, bodyLength])

def main():
    mapper()

if __name__ == "__main__":
    main()
