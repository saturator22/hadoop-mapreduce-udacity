#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    data = re.search(r'([(\d\.)]+) (.*) (.*) \[(.*)\] "(.*)" (.*) (.*)', line).groups()

    if len(data) == 7:
        ip, identity, username, dateTime, request, status, objectSize = data
        request_parts = request.split(" ")
        url = request_parts[1]
        print url

