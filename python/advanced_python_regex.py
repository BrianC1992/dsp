
import pandas as pd
import numpy as np

#cleaning punctiations on degree titles
faculty = pd.read_csv('/home/brianc/ds/metis/prework/dsp/python/faculty.csv')
faculty.columns = ['name','degree','title','email']
faculty["degree"] =faculty["degree"].str.strip().str.replace('Ph.D.','PhD').str.replace('Ph.D','PhD').str.replace('PhD', 'Ph.D.')
faculty["degree"]=faculty["degree"].str.strip().str.replace('ScD','Sc.D.').str.replace('MS','M.S.')

#Determining the number of degrees
degCount = faculty.groupby(['degree'],as_index = False).count()
degCount=degCount.drop(['title','email'],axis = 1)
degCount.rename(columns={'name':'count'},inplace = True)
degCount= pd.concat([pd.Series(row['count'], row['degree'].split(" "))for _, row in degCount.iterrows()]).reset_index()             
degCount = degCount.groupby(['index'],as_index = False).sum() 
degCount.columns = ['degree','count']
degCount

#Determining the number of Rank titles
degTitle = faculty.groupby(['title'],as_index = False ).count()
degTitle["title"]=degTitle["title"].str.strip().str.replace('Assistant Professor is Biostatistics','Assistant Professor of Biostatistics')
degTitle = degTitle.groupby(['title'],as_index = False ).sum()
degTitle = degTitle.drop(['degree','email'],axis = 1)
degTitle.rename(columns={'name':'count'},inplace = True)
degTitle

#Making email list
email = faculty['email'].tolist()
email

#Determining the number of domains
domain = faculty.groupby(['email'],as_index = False).count()
domain['email'] = domain['email'].str.strip().str.replace(r'.+\@', " " )
domainCount = domain.groupby(['email'],as_index = False).sum()
domainCount = domainCount.drop(['degree','title'],axis = 1)
domainCount.columns = ['domain','count']
domainCount
