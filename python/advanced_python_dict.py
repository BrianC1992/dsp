# Qestion 6
import pandas as pd
import numpy as np
import re
faculty = pd.read_csv('/home/brianc/ds/metis/prework/dsp/python/faculty.csv')
faculty.columns = ['name','degree','title','email']
faculty["degree"] =faculty["degree"].str.strip().str.replace('Ph.D.','PhD').str.replace('Ph.D','PhD').str.replace('PhD', 'Ph.D.')
faculty["degree"]=faculty["degree"].str.strip().str.replace('ScD','Sc.D.').str.replace('MS','M.S.')
firstLast =(r'(.+)\s(.+)')
faculty[['FirstName','LastName']]=faculty['name'].str.extract(firstLast, expand = True)
faculty.drop(['name','FirstName'], axis=1, inplace=True)
mydict = {}
for x in range(len(faculty)):
    currentid = faculty.iloc[x,3]
    currentvalue = faculty.iloc[x,0:3]
    mydict.setdefault(currentid, [])
    mydict[currentid].append(currentvalue)
first3pairs = {k: mydict[k] for k in list(mydict.keys())[:3]}
first3pairs

#Question 7
import pandas as pd
import numpy as np
import re

faculty = pd.read_csv('/home/brianc/ds/metis/prework/dsp/python/faculty.csv')
faculty.columns = ['name','degree','title','email']
faculty["degree"] =faculty["degree"].str.strip().str.replace('Ph.D.','PhD').str.replace('Ph.D','PhD').str.replace('PhD', 'Ph.D.')
faculty["degree"]=faculty["degree"].str.strip().str.replace('ScD','Sc.D.').str.replace('MS','M.S.')
firstLast =(r'(.+)\s(.+)')
faculty[['FirstName','LastName']]=faculty['name'].str.extract(firstLast, expand = True)
faculty.drop(['name'], axis=1, inplace=True)
faculty = faculty[['FirstName','LastName','degree','title','email']]
mydict = faculty.set_index(['FirstName','LastName']).T.to_dict()
      
first3pairs = {k: mydict[k] for k in sorted(mydict.keys())[:3]}
first3pairs

#Question 8
faculty = pd.read_csv('/home/brianc/ds/metis/prework/dsp/python/faculty.csv')
faculty.columns = ['name','degree','title','email']
faculty["degree"] =faculty["degree"].str.strip().str.replace('Ph.D.','PhD').str.replace('Ph.D','PhD').str.replace('PhD', 'Ph.D.')
faculty["degree"]=faculty["degree"].str.strip().str.replace('ScD','Sc.D.').str.replace('MS','M.S.')
firstLast =(r'(.+)\s(.+)')
faculty[['FirstName','LastName']]=faculty['name'].str.extract(firstLast, expand = True)
faculty.drop(['name'], axis=1, inplace=True)
faculty = faculty[['LastName','FirstName','degree','title','email']]
faculty = faculty.sort(['LastName','FirstName'])
mydict = faculty.set_index(['LastName','FirstName']).T.to_dict()

first3pairs = {k: mydict[k] for k in sorted(mydict.keys())[:3]}
first3pairs
