#!/usr/bin/python
import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')

    currentPost = None
    postQuestionAnswerLengths = {}

    for line in reader:
        postId = line[0]
        nodeType = line[1]
        bodyLength = int(line[2])
        
        if currentPost and currentPost != postId and len(postQuestionAnswerLengths) > 0:
            writeOutput(currentPost, postQuestionAnswerLengths)

            postQuestionAnswerLengths = {}
        
        currentPost = postId

        postQuestionAnswerLengths = fillPostQuestionAnswerLengths(nodeType, bodyLength, postQuestionAnswerLengths)
    
    writeOutput(currentPost, postQuestionAnswerLengths)
    
def fillPostQuestionAnswerLengths(nodeType, bodyLength, postQuestionAnswerLengths):        
    if nodeType == "question":
        postQuestionAnswerLengths["Q"] = bodyLength
    elif nodeType == "answer":
        if "A" not in postQuestionAnswerLengths:
            postQuestionAnswerLengths["A"] = [bodyLength]
        else:
            postQuestionAnswerLengths["A"].append(bodyLength)
    return postQuestionAnswerLengths

def writeOutput(authorId, postQuestionAnswerLengths):
    writer = csv.writer(sys.stdout, delimiter='\t')
    
    questionBodyLength = postQuestionAnswerLengths["Q"]
    avgAnswerLength = 0    
    
    if "A" in postQuestionAnswerLengths:
        answerBodyLengths = postQuestionAnswerLengths["A"]
        if answerBodyLengths > 0:
            avgAnswerLength = sum(answerBodyLengths)/float(len(answerBodyLengths))

    writer.writerow([authorId, questionBodyLength, avgAnswerLength])            

def main():
    reducer()

if __name__ == "__main__":
    main()
