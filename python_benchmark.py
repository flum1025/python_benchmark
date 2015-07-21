'''
Created on 2015/07/21

@author: flum
'''
import time
import datetime
from datetime import datetime
import math
import string
import random

str_num = range(10)
times = range(100000000)

start = datetime.now()
print 'start : ' + str(start.minute) + ':' + str(start.second) + '.' + str(start.microsecond)

for var in times:
    ''.join([random.choice(string.ascii_letters + string.digits) for i in str_num])

end = datetime.now()
print 'end : ' + str(end.minute) + ':' + str(end.second) + '.' + str(end.microsecond)

margin = end - start
marginsec = margin.seconds
marginmin = math.floor(marginsec / 60)
print 'margin : ' + str(marginmin) + ':' + str(marginsec - marginmin)