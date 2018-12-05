#!/usr/bin/python
import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        body = line[4]
        
        if bodyHasNoPunctuationMarks(body):
            writer.writerow(line)
        elif isPunctuationMarkAtTheEndOfBody(body) and bodyHasOnlyOnePunctuationMark(body):
            writer.writerow(line)

def bodyHasNoPunctuationMarks(body):
    if '?' not in body and '.' not in body and '!' not in body:
        return True
    
    return False
    
def bodyHasOnlyOnePunctuationMark(body):
    dotCount = countPunctuationMark(body, '.')
    questionCount = countPunctuationMark(body, '?')
    exclamationCount = countPunctuationMark(body, '!')
    
    countSum = dotCount + questionCount + exclamationCount
    
    if countSum == 1:
        return True
        
    return False
    
def countPunctuationMark(body, punctuationMark):
    return body.count(punctuationMark)

def isPunctuationMarkAtTheEndOfBody(body):
    lastChar = body[-1]
    
    if lastChar == '.' or lastChar == '?' or lastChar == '!':
        return True
    
    return False

test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"This is one sentence\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Also one sentence!\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Hey!\nTwo sentences!\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"One. Two! Three?\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"One Period. Two Sentences\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Three\nlines, one sentence\n\"\t\"\"
"""

# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
