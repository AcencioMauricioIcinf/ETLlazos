#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas, csv

revise = None

with open('Ivette  Pascual Robin/red.csv', mode='r') as archivo:
	revise1 = [line.replace('\0','').replace('\r','').replace('\n','') for line in archivo]
	revise = [line for line in revise1[1:] if line.strip()]
print revise1
print revise
for l in revise:
	print "-> %s" % l
print "Done"

# ~ with open('test2.csv', 'w') as myfile:
    # ~ wr = csv.writer(myfile)
    # ~ for r in revise:
		# ~ wr.writerow(r.split(","))
