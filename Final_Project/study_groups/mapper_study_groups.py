#!/usr/bin/python
import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')
    
    for line in reader:
        nodeType = line[5]
        authorId = line[3]
        questionPostId = None

        if nodeType == "question":
            questionPostId = line[0]
        elif nodeType == "answer":
            questionPostId = line[6]
        elif nodeType == "comment":
            questionPostId = line[7]
        else:
            continue        

        writer.writerow([questionPostId, authorId])

def main():
    mapper()

if __name__ == "__main__":
    main()
