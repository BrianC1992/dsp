import csv
import pandas as pd
faculty = pd.read_csv('/home/brianc/ds/metis/prework/dsp/python/faculty.csv')
faculty.columns = ['name','degree','title','email']
faculty["degree"] =faculty["degree"].str.strip().str.replace('Ph.D.','PhD').str.replace('Ph.D','PhD').str.replace('PhD', 'Ph.D.')
faculty["degree"]=faculty["degree"].str.strip().str.replace('ScD','Sc.D.').str.replace('MS','M.S.')
faculty.email.to_csv('emails.csv', header=False, index=False)
