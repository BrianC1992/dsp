# Hint:  use Google to find python function

####a) 
from datetime import datetime
date_format = "%m-%d-%Y"
date_start = '01-02-2013'    
date_stop = '07-28-2015'

data_start = datetime.strptime(date_start, date_format)
data_stop = datetime.strptime(date_stop, date_format)

delta = data_stop-data_start

print(delta.days)

####b)  from datetime import datetime
date_format = "%m%d%Y"
date_start = '12312013'    
date_stop = '05282015' 

data_start = datetime.strptime(date_start, date_format)
data_stop = datetime.strptime(date_stop, date_format)

delta = data_stop-data_start

print(delta.days)

####c)  
from datetime import datetime
date_format = "%d-%b-%Y"
date_start = '15-Jan-1994'    
date_stop = '14-Jul-2015' 

data_start = datetime.strptime(date_start, date_format)
data_stop = datetime.strptime(date_stop, date_format)

delta = data_stop-data_start

print(delta.days) 
