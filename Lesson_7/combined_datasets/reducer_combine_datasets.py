#!/usr/bin/python

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    currentUser = None
    currentUserData = None
    currentUserPostData = {}

    for line in reader:
        
        userId = line[0]
        
        if not userId.isdigit():
            continue
        
        if currentUser and currentUser != userId and currentUserData and len(currentUserPostData) > 0:

            writeCombinedData(writer, currentUserData, currentUserPostData)

            currentUserData = None
            currentUserPostData = {}
            
        currentUser = userId
        
        if line[1] == "U":
            userId, dataIdentifier, reputation, gold, silver, bronze = line
            currentUserData = [reputation, gold, silver, bronze]
        elif line[1] == "N":
            userId, dataIdentifier, postId, title, tagnames, nodeType, parentId, \
            absParentId, addedAt, score = line        
            currentUserPostData[postId] = [postId, title, tagnames, userId, nodeType, \
                                           parentId, absParentId, addedAt, score]

    writeCombinedData(writer, currentUserData, currentUserPostData)    

def writeCombinedData(writer, userData, userPostData):
    for postId in userPostData:
        userPost = userPostData[postId]
        combinedData = userPost + userData
        writer.writerow(combinedData)

def main():
    reducer()

if __name__ == "__main__":
    main()
        
