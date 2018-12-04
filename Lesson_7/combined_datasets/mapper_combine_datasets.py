#!/usr/bin/python

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', \
                        quoting=csv.QUOTE_ALL)

    for line in reader:

        if len(line) == 5:
            writer.writerow(mapForumUserData(line))
        elif len(line) == 19:
            writer.writerow(mapForumNodeData(line))

def mapForumNodeData(line):
    dataIdentifier = "N"
    postId, title, tagnames, userId, body, nodeType, parentId, absParentId, \
    addedAt, score, stateString, lastEditedId, lastActivityById, lastActivityBy, \
    activeRevisionId, extra, extraRefId, extraCount, marked = line
    
    return [userId, dataIdentifier, postId, title, tagnames, nodeType, parentId, \
            absParentId, addedAt, score]

def mapForumUserData(line):
    dataIdentifier = "U"
    userId, reputation, gold, silver, bronze = line
    
    return [userId, dataIdentifier, reputation, gold, silver, bronze]
    
def main():
    mapper()

if __name__ == "__main__":
    main()


        
