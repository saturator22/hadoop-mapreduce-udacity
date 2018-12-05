#!/usr/bin/python
import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')

    currentPost = None
    authorsId = []

    for line in reader:
        postId = line[0]
        authorId = int(line[1])
        
        if currentPost and currentPost != postId and len(authorsId) > 0:
            writeOutput(currentPost, authorsId)

            authorsId = []
        
        currentPost = postId

        authorsId = fillPostIdAuthorsId(authorId, authorsId)
    
    writeOutput(currentPost, authorsId)
    
def fillPostIdAuthorsId(authorId, authorsId):
    
    if authorId not in authorsId:
        authorsId.append(authorId)

    return authorsId

def writeOutput(postId, authorsId):
    writer = csv.writer(sys.stdout, delimiter='\t')
    
    if len(authorsId) == 0:
        authorsId = ["None"]

    writer.writerow([postId, authorsId])            

def main():
    reducer()

if __name__ == "__main__":
    main()
