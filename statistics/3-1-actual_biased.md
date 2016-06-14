[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>>   

```  
%matplotlib inline
import chap01soln
resp = chap01soln.ReadFemResp()
import thinkstats2
import thinkplot
pmf1 = thinkstats2.Pmf(resp['numkdhh'])
thinkplot.Pmf(pmf1,label='numkdhh')
thinkplot.Show(xlabel = 'Number of Children under 18') 
def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf  
biased_pmf = BiasPmf(pmf1, label='observed')  
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf1, biased_pmf])
thinkplot.Show(xlabel='Number of Children Under 18', ylabel='PMF')
pmf1.Mean()
biased_pmf.Mean()
```
Answers to questions:  
![github logo](images/output_5_0.png)
![github logo](images/output_11_0.png)


