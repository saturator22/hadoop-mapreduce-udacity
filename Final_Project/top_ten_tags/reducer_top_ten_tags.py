#!/usr/bin/python
import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')

    tagFrequency = {}

    for line in reader:
        tag = line[0]
        tagOccurance = int(line[1])

        if tag not in tagFrequency:
            tagFrequency[tag] = tagOccurance
        else:
            tagFrequency[tag] += tagOccurance

    topTenTags = sorted(tagFrequency.items(), key=lambda x: -x[1])[:10]

    for tag in topTenTags:
        writer.writerow([tag[0], tag[1]])

def main():
    reducer()

if __name__ == "__main__":
    main()
