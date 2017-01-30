#!/usr/bin/python

import sys

#Write a Map Reduce program to find the monetary value of the highest individual sale for each seperate store (Reno, Toledo, Chandler). 

prev_location = None
max_sales = 0.00

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    location, value = data_mapped

    if prev_location and prev_location != location:
	print "{0}\t{1}".format(prev_location, max_sales)
        prev_location = location
	max_sales = float(value)
	continue
	
    prev_location = location
    if value > max_sales: max_sales = float(value)

print "{0}\t{1}".format(location, max_sales)
	

