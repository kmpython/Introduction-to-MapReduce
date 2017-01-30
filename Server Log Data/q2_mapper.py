#!/usr/bin/python
import sys
import re

#Write a Map Reduce program to determine the number of hits to the site made by each different ip address.

ip_dict = {}
p = re.compile(
    '([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)'
    )

for line in sys.stdin:
    data = line.strip()
    data_list = []
    try:
        result = p.match(data)
        host, ignore, user, date, request, status, size = result.groups()
	method, page, query_strig = request.split(" ")
	if page == "/assets/js/the-associates.js":
		print "{0}\t{1}".format(page, 1)
    except: continue

