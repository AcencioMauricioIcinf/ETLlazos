#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas, csv

df = pandas.read_csv('Ivette  Pascual Robin/red (copy).csv')
print df
with open('Ivette  Pascual Robin/red (copy).csv', mode='r') as archivo:
	csvreader = csv.reader(archivo)
	for row in csvreader:
		print row
