#!/usr/bin/python

#Write a Map Reduce program to breakdown the sales by product category (Toys, Consumer Electronics) across all stores

import sys

prev_item = None
total_sales = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    item, value = data_mapped

    if prev_item and prev_item != item:
        print "{0}\t{1}".format(prev_item, total_sales)
	prev_item = item
	total_sales = 0

    prev_item = item
    total_sales += float(value)

print "{0}\t{1}".format(item, total_sales)
	

