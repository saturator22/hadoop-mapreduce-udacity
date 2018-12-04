#!/usr/bin/python

import sys

wordStatistics = {}    

for line in sys.stdin:
    mappedData = line.split("\t")
    
    nodeId = int(mappedData[0].strip())
    word = mappedData[1].strip().lower()

    if word not in wordStatistics:
        nodeSet = set()
        nodeSet.add(nodeId)
        wordStatistics[word] = [1, nodeSet]
    else:
        wordStatistics[word][0] += 1
        wordStatistics[word][1].add(nodeId)

for key in wordStatistics:
    print key, ":::NumberOfOccurences:::", wordStatistics[key][0], ":::NodeIds:::", \
            sorted(wordStatistics[key][1])     

