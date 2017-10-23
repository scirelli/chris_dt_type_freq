#!/usr/bin/python3

import pandas as pd
import datetime 
import pprint
import time

File_1 = pd.read_csv(r'./COF.csv')
df1 = pd.DataFrame(File_1)

print('File loaded.')

pp = pprint.PrettyPrinter(indent=4)
t0 = time.clock()
result = getDataframeDataTypesPerColumn(df1)
t1 = time.clock()
total = t1 - t0
pp.pprint(result)
print('Ran in ' + str(total) + 's')
