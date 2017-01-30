#!/usr/bin/python

import sys

#Write a Map Reduce program to find the total number of sales and the sales value from all the stores

count = 0
totalSales = 0
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        count = count + 1
        totalSales = totalSales + float(cost)

print "{0}\t{1}".format(count, totalSales)

