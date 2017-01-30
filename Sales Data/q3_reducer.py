#!/usr/bin/python

import sys

#Write a Map Reduce program to find the total number of sales and the sales value from all the stores

SalesCount = 0
SalesValue = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    MapSalesCnt = 0
    MapSalesVal = 0
    MapSalesCnt, MapSalesVal = data_mapped
    print MapSalesCnt, "\t", MapSalesVal

    SalesCount = SalesCount + int(MapSalesCnt)
    SalesValue = SalesValue + float(MapSalesVal)

print SalesCount, "\t", SalesValue
