#!/usr/bin/python

import sys
import re

urlToRemove = "http://www.the-associates.co.uk"

for line in sys.stdin:
    data = re.search(r'([(\d\.)]+) (.*) (.*) \[(.*)\] "(.*)" (.*) (.*)', line).groups()

    if len(data) == 7:
        ip, identity, username, dateTime, request, status, objectSize = data
        parsedRequest = request.split(" ")
        url = parsedRequest[1]
	
    if urlToRemove in url:
        url = url.replace(urlToRemove, '')

    print url

