[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> The code for the Cohen's d problem is below:  

```
import nsfg
import numpy as np
import sys
import thinkstats2
import math
import first

df = nsfg.ReadFemPreg()
df
pregStats = df.reindex(columns=['pregordr','pregend1','totalwgt_lb'])
pregStats = pregStats.dropna()

pregWt = pregStats[pregStats['pregordr']==1]
del pregWt['pregordr']
pregWt = pregWt.reset_index()

pregWt2 = pregStats[pregStats['pregordr']!=1]
pregWt2 = pregWt2.rename(columns={'pregend1':'pregEndOthers'})
del pregWt2['pregordr']
pregWt2 = pregWt2.reset_index()

def CohenEffect(x1,x2):   
    diff = x1.mean() - x2.mean()

    var1 = x1.var()
    var2 = x2.var()
    n1, n2 =len(x1), len(x2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
   
    return print('Cohens d equals:', d) 
    
   
CohenEffect(pregWt['totalwgt_lb'],pregWt2['totalwgt_lb'])
CohenEffect(pregWt['pregend1'],pregWt2['pregEndOthers'])  

```
Cohens d equals: -0.06911962316626086 for Birth order
  


