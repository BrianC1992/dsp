[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>>    
```  
from __future__ import print_function, division
import thinkstats2
import thinkplot
import scipy.stats
%matplotlib inline 
# inserting parameter values
muMale = 178 # centimeters
sigmaMale = 7.7 # centimeters
BMGLowEng = 70 #inches
BMGHighEng = 73 #inches
# Converting English to Metric Units
def convertEM(Eng):
    Metric = Eng * 2.254
    return Metric  
# Converting to z-scores
def zTrans(x,mu,sigma):
    z = (x-mu)/sigma
    return z 
BMGLMetric = convertEM(BMGLowEng)
BMGHMetric = convertEM(BMGHighEng)  
zHigh = zTrans(BMGHMetric,muMale,sigmaMale)
zLow = zTrans(BMGLMetric,muMale,sigmaMale)  
percent = scipy.stats.norm.cdf(zHigh)-scipy.stats.norm.cdf(zLow)
print("The precentage of US men in the range to join the Blue Man Group is:", percent*100, "%")  
```   
The precentage of US men in the range to join the Blue Man Group is: 3.59299370403 %
