# Hint:  use Google to find python function

####a) 
from datetime import datetime
date_format = "%m-%d-%Y"
date_start = '01-02-2013'  
date_stop = '07-28-2015' 
data_start = datetime.strptime('01-02-2013', date_format)
data_stop = datetime.strptime('07-28-2015', date_format)

delta = data_stop-data_start

print(delta.days)

####b)  
date_start = '12312013'  
date_stop = '05282015'  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
