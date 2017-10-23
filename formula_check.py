#!/usr/bin/python3

import pandas as pd
import datetime 
import pprint
import time

File_1 = pd.read_csv(r'./COF.csv')
df1 = pd.DataFrame(File_1)

print('File loaded.')

def getDataframeDataTypes(df):
	d = dict()
	t = None
	for row in df.itertuples(index=True, name='Pandas'):
		for x in row:
			t = type(x).__name__
			if(t in d):
				d[t] += 1
			else:
				d[t] = 1
	return d

def getDataframeDataTypesPerColumn(df):
	cols = dict()
	t = None
	for row in df.itertuples(index=False):
		for (columnName, value) in row._asdict().items():
			t = type(value).__name__

			if(columnName in cols):
				d = cols[columnName]
				if(t in d):
					d[t] += 1
				else:
					d[t] = 1
			else:
				cols[columnName] = dict()
				d = cols[columnName]
				d[t] = 1
	return cols

pp = pprint.PrettyPrinter(indent=4)
t0 = time.clock()
result = getDataframeDataTypesPerColumn(df1)
t1 = time.clock()
total = t1 - t0
pp.pprint(result)
print('Ran in ' + str(total) + 's')
