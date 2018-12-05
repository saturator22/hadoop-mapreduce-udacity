#!/usr/bin/python
import sys
import csv

from datetime import datetime

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')
    
    for line in reader:
        authorId = line[3]
        
        if not authorId.isdigit():
            continue

    	date = line[8]
        hour = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f+00").hour

        writer.writerow([authorId, hour])

def main():
    mapper()

if __name__ == "__main__":
    main()
