#!/usr/bin/python

import sys

#Write a Map Reduce program to find the most popular file - that is the file whose path occurs most often in the data. 
#IMPORTANT: some pathnames begin with "http://www.the-associates.co.uk". Please remove the portion so that all occurences of a file are counted.
#We are using urlprase - a built in python function to seperate the pathnames.

prev_doc = None
max_doc = None
total_count = 0
hit_count = 0
max_count = 0

for line in sys.stdin:
	doc_data = line.strip().split("\t")
	if len(doc_data) != 2: continue
	
	doc, hit_count = doc_data
	
	if prev_doc and doc != prev_doc:
		if total_count > max_count:
			max_doc = prev_doc
			max_count = total_count
		total_count = 0

	prev_doc = doc
	total_count = total_count + int(hit_count)

print "{0}\t{1}".format(max_doc, max_count)
	
		
