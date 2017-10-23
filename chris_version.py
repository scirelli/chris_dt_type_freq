#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 07:32:25 2017

@author: Chris.Cirelli
"""

##############  PAGCKAGES   ##################################
import pandas as pd
import datetime 
import pprint
import time

##############  DATA FILES   #################################
File_1 = pd.read_csv(r'./COF.csv')
df1 = pd.DataFrame(File_1)

print('File loaded.')
 
# File_1 = pd.read_excel(r'C:\Users\Chris.Cirelli\Desktop\Python Programing Docs\GSU\FInal Project\df2_policy data.xlsx')
# df1 = pd.DataFrame(File_1)

##############  REUSABLE FORMULAS   #################################

def shit_head(dataframe):
    Dictionary = {}
    List1 = []
    for x in dataframe:
        Dictionary[x] = [type(x) for x in df1[x]]
    df_beg = pd.DataFrame(Dictionary)
    for x in df_beg:
        List1.append(df_beg[x].value_counts())
    df_end = pd.DataFrame(List1)
    return df_end

pp = pprint.PrettyPrinter(indent=4)
t0 = time.clock()
result = shit_head(df1)
t1 = time.clock()
total = t1 - t0
pp.pprint(result)
print('Ran in ' + str(total) + 's')
